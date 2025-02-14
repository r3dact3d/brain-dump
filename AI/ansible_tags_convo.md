# Ansible Tags Not Working

When encountering issues with Ansible tags not working as expected, it's important to understand how tags are applied and inherited in Ansible. Here are some common issues and their solutions:

1. **Tag Inheritance with `include_role` and `include_tasks`:**
   - By default, Ansible does not apply tag inheritance to dynamic reuse with `include_role` and `include_tasks`. This means that if you add tags to an include, they apply only to the include itself, not to any tasks in the included file or role.
   - To enable tag inheritance, you can use the `apply` keyword or wrap the include tasks in a block. For example:
     ```yaml
     - name: Apply the db tag to the include and to all tasks in db.yml
       include_tasks:
         file: db.yml
         # adds 'db' tag to tasks within db.yml
         apply:
           tags: db
       # adds 'db' tag to this 'include_tasks' itself
       tags: db
     ```

2. **Using `import_role` and `import_tasks`:**
   - If you want tag inheritance, you should use `import_role` and `import_tasks` instead of `include_role` and `include_tasks`. This ensures that the tags are applied to all tasks within the imported role or tasks file.
   - Example:
     ```yaml
     - hosts: webservers
       tasks:
         - name: Import the foo role
           import_role:
             name: foo
           tags:
             - bar
             - baz
     ```

3. **Tagging Tasks and Roles:**
   - You can add tags to individual tasks, blocks, plays, roles, or imports. Tags do not select or skip tasks; they only define tags for tasks.
   - Example:
     ```yaml
     - name: Install ntp
       ansible.builtin.yum:
         name: ntp
         state: present
       tags: ntp
     ```

4. **Special Tags:**
   - Ansible reserves several tag names for special behavior: `always`, `never`, `tagged`, `untagged`, and `all`.
   - The `always` tag ensures a task or play always runs unless explicitly skipped with `--skip-tags always`.
   - Example:
     ```yaml
     - block:
         - name: Include tasks from db.yml
           include_tasks: db.yml
       tags: always
     ```

5. **Command Line Usage:**
   - To run or skip tasks based on tags, use the `--tags` and `--skip-tags` options when running the playbook.
   - Example:
     ```bash
     ansible-playbook playbook.yml --tags ntp
     ```

If you are still facing issues, ensure that your playbook and roles are correctly structured and that you are using the correct methods for including and tagging tasks.
