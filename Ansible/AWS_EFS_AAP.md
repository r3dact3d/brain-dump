---
type: ansible-note
---

# AWS EFS on AAP 2.5

## New Fabric Response

To configure AWS Elastic File System (EFS) for shared storage with Red Hat Ansible Automation Platform (AAP) running as a container, you need to follow a few steps to ensure proper integration. Below are three possible solutions, ordered from best to worst, along with explanations and potential issues.

### Solution 1: Use Docker Volumes with EFS

**Explanation:**
This solution involves mounting the EFS volume directly to the Docker container using Docker volumes. This is a straightforward approach that leverages Docker's built-in support for EFS.

**Steps:**
1. Create an EFS file system in AWS.
2. Create an EFS mount target in your VPC.
3. Install the AWS CLI and Docker on your host machine.
4. Configure Docker to use the EFS volume:

```bash
docker volume create --driver local \
  --opt type=efs \
  --opt device=<EFS_FILE_SYSTEM_ID> \
  --opt o=tls \
  --opt t=nfs4 \
  efs-volume
```

5. Run the AAP container with the EFS volume:

```bash
docker run -d \
  --name aap \
  --mount source=efs-volume,target=/path/to/shared/storage \
  your-aap-image
```

**Potential Issues:**
- Ensuring that the EFS mount target is accessible from the Docker host.
- Managing permissions and security groups for the EFS.

**Source:** [AWS Documentation](https://docs.aws.amazon.com/efs/latest/ug/using-docker-volumes.html)

### Solution 2: Use NFS Client Provisioner in Kubernetes

**Explanation:**
If you are using Kubernetes to manage your Docker containers, you can use the NFS Client Provisioner to mount the EFS volume.

**Steps:**
1. Deploy the NFS Client Provisioner in your Kubernetes cluster.
2. Create a PersistentVolume (PV) and PersistentVolumeClaim (PVC) for the EFS:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    path: /
    server: <EFS_FILE_SYSTEM_ID>.efs.<region>.amazonaws.com
```

3. Create a PVC to claim the EFS volume:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  volumeName: efs-pv
```

4. Deploy the AAP container with the PVC:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: aap
spec:
  replicas: 1
  selector:
    matchLabels:
      app: aap
  template:
    metadata:
      labels:
        app: aap
    spec:
      containers:
      - name: aap
        image: your-aap-image
        volumeMounts:
        - mountPath: /path/to/shared/storage
          name: efs-storage
      volumes:
      - name: efs-storage
        persistentVolumeClaim:
          claimName: efs-pvc
```

**Potential Issues:**
- Ensuring that the EFS mount target is accessible from the Kubernetes nodes.
- Managing permissions and security groups for the EFS.

**Source:** [Kubernetes Documentation](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#nfs)

### Solution 3: Use a Sidecar Container

**Explanation:**
This solution involves using a sidecar container to mount the EFS volume and then sharing it with the AAP container using a shared volume.

**Steps:**
1. Create a sidecar container that mounts the EFS volume:

```bash
docker run -d \
  --name efs-sidecar \
  --mount type=volume,source=efs-volume,target=/path/to/shared/storage \
  -v /path/to/shared/storage:/path/to/shared/storage \
  your-sidecar-image
```

2. Run the AAP container with the shared volume:

```bash
docker run -d \
  --name aap \
  --network container:efs-sidecar \
  --mount type=bind,source=/path/to/shared/storage,target=/path/to/shared/storage \
  your-aap-image
```

**Potential Issues:**
- Managing the lifecycle of the sidecar container.
- Ensuring that the shared volume is correctly mounted and accessible.

**Source:** [Docker Documentation](https://docs.docker.com/storage/volumes/)

Each solution has its own advantages and potential issues. The best approach depends on your specific environment and requirements.


## First response

Deploying Red Hat Ansible Automation Platform (AAP) 2.5 in a containerized environment with AWS EFS (Elastic File System) storage involves several steps. Below is a detailed guide to help you through the process:

Prerequisites
AWS Account: Ensure you have an AWS account with appropriate permissions.
EFS File System: Create an EFS file system in your AWS account.
IAM Roles and Policies: Ensure that your EC2 instances have the necessary IAM roles and policies to access the EFS file system.
Ansible Automation Platform: Download the AAP 2.5 installation bundle.
Steps to Deploy AAP 2.5 with AWS EFS Storage
1. Create an EFS File System
Log in to the AWS Management Console.
Navigate to the EFS service.
Create a new file system and note down the File System ID.
2. Mount the EFS File System
Ensure that your EC2 instances have the amazon-efs-utils package installed.

```bash
sudo yum install -y amazon-efs-utils
Mount the EFS file system on your EC2 instances.

sudo mount -t efs -o tls <file-system-id>:/ /mnt/efs
```

3. Update the Inventory File
Open your Ansible inventory file.
Add the EFS mount point to the inventory file under the [all:vars] section.

```yaml
[all:vars]
efs_mount_point=/mnt/efs
```

4. Configure AAP to Use EFS Storage
Edit the AAP configuration files to use the EFS mount point for storage.
Update the automation-controller, private-automation-hub, and execution-environment configurations to use the EFS mount point.
5. Deploy AAP
Run the Ansible playbook to deploy AAP.

```bash
ansible-playbook -i inventory setup.yml
```
Example Inventory File
Here is an example of what your inventory file might look like:

```yaml
[automationcontroller]
controller.example.com ansible_host=<controller-ip>

[database]
database.example.com ansible_host=<database-ip>

[all:vars]
efs_mount_point=/mnt/efs
admin_password='your_admin_password'
pg_password='your_pg_password'

[automationcontroller:vars]
controller_route_host_vars=true
controller_route_host_default_value='controller.example.com'
```

Example Playbook
Here is an example playbook snippet to mount the EFS file system:

```yaml
- name: Mount EFS file system
  hosts: all
  become: yes
  tasks:
    - name: Install amazon-efs-utils
      yum:
        name: amazon-efs-utils
        state: present

    - name: Mount EFS
      mount:
        path: "{{ efs_mount_point }}"
        src: "<file-system-id>:/"
        fstype: efs
        opts: tls
        state: mounted
```

Best Practices
Security: Ensure that your EFS file system is secured with appropriate IAM policies and security groups.
Monitoring: Set up monitoring for your EFS file system to track usage and performance.
Backups: Regularly back up your EFS data to prevent data loss.
By following these steps, you should be able to deploy AAP 2.5 in a containerized environment with AWS EFS storage successfully. If you encounter any issues or have specific questions, feel free to ask!


