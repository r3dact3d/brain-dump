---
type: demo-note
description: This is my demo template
---

# AAP Walkthrough_24

Hello and welcome, my name is Brady Thompson and I am a Consulting Architect at Red Hat. Today I will walk through at a high-level the Automation Controller component of the Ansible Automation Platform, and highlight some of the Controller options and features that give us the ability to achieve robust Enterprise Automation at Scale.

## Dashboard Overview

The Dashboard provides:
* A big picture view of your hosts, inventories, and projects being automated across your enterprise
  * Each of these is linked to the corresponding resource in the controller
  * Failed jobs can be easily filtered and identified

## Jobs View

The Jobs view displays:
* All jobs that have run in the controller, including:
  * Projects
  * Templates
  * Management jobs
  * Playbook runs
* Easy filtering options by launcher and job name
* Detailed job information including:
  * Job executor
  * Variables passed
  * Exact playbook revision
  * Complete playbook run output

## Schedules and Workflow Approvals

### Schedules
* Shows all scheduled jobs and their status

### Workflow Approvals
* Create workflows with integrated approval processes
* View pending approvals
* Implement custom notifications (email or chat)

## Access Management

The Access section provides organizational and security controls:
* Administrator capabilities:
  * User setup and management
  * Permission configuration
  * Credential management
  * Automation execution controls
* Organizational structure support:
  * Team-based access control for individual resources
  * Organization-level access control for controller administration
* Integration with identity management:
  * LDAP support
  * Active Directory integration

## Core Components

### Credentials
* Integration with Secret Managers:
  * HashiCorp Vault
  * CyberVault
* Custom credential type creation capabilities

### Projects
* Logical collections of Ansible Playbooks
* Version control repository integration
* Focused on organizational collaboration and sharing
* Community-created automation support
* Red Hat certified content availability

### Hosts
* Support for various target types:
  * Servers
  * Network devices
  * Cloud resources
* Agentless architecture benefits:
  * No installation requirements
  * Broad automation capabilities

### Inventories
* Logical collections of hosts
* Features include:
  * Group organization
  * Smart dynamic inventory support
  * Domain-based segmentation
  * Use case segregation

## Templates

### Template Components
* Integration of:
  * Inventories
  * Credentials
  * Projects

### Execution Environments
* Container-based implementation
* Benefits:
  * Certified Ansible versions
  * Consistent Python dependencies
  * Streamlined testing environments
  * Simplified maintenance
* Template-specific customization options

### Additional Features
* Survey capability for variable collection
* Scheduling options
* Identity and access controls
