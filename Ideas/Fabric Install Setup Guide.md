---
type: idea-note
description: This is my idea note template
---

# Fabric Installation and Setup Guide

## Introduction

Fabric is a powerful tool designed to streamline various technical tasks by integrating AI vendors and tools. This guide will walk you through the installation and setup process on a Fedora 41 laptop.

## Installation

### Step 1: Download Fabric

First, download the Fabric binary from the GitHub releases page.

```bash
$ curl -L https://github.com/danielmiessler/fabric/releases/latest/download/fabric-linux-amd64 > fabric && chmod +x fabric && ./fabric --version
```

> **Note:** Ensure that `/home/r3dact3d/bin/` is included in your `$PATH`. You can check your current `$PATH` with:
> ```bash
> $ echo $PATH
> ```
> If not, add it by running:
> ```bash
> $ cd
> $ mkdir bin
> $ mv fabric bin/
> $ fabric --help
> ```

## Setup

### Step 2: Initial Setup

Run the initial setup to configure Fabric.

```bash
$ fabric --setup
```

> You should see something like the output below without the already **configured** options.

```bash
Available plugins (please configure all required plugins)::

AI Vendors [at least one, required]

	[1]	OpenAI
	[2]	Ollama (configured)
	[3]	Azure
	[4]	Groq
	[5]	Gemini
	[6]	Anthropic
	[7]	SiliconCloud
	[8]	OpenRouter
	[9]	Mistral (configured)

Tools

	[10]	Default AI Vendor and Model [required] (configured)
	[11]	Patterns - Downloads patterns [required] (configured)
	[12]	YouTube - to grab video transcripts and comments (configured)
	[13]	Language - Default AI Vendor Output Language (configured)
	[14]	Jina AI Service - to grab a webpage as clean, LLM-friendly text (configured)

[Plugin Number] Enter the number of the plugin to setup (leave empty to skip):
```

### Step 3: Configure AI Vendors

Essentially, select the AI vendor you want to use. For this example, we'll use Mistral and I'll configure my local Ollama instance.  Then configure the tools you want to use.

```bash
[Plugin Number] Enter the number of the plugin to setup (leave empty to skip): 9
```

Enter your Mistral API key and base URL.

```bash
[Mistral]
Enter your Mistral API KEY (leave empty to skip): "***********************************Uni"
Enter your Mistral API BASE URL (leave empty for 'https://api.mistral.ai/v1' or type 'reset' to remove the value):
```

### Step 4: Configure Tools

Select the default AI vendor and model.

```bash
[Plugin Number] Enter the number of the plugin to setup (leave empty to skip): 10
```

Choose the model you want to use.

```bash
Available models:

Mistral

	[1]	ministral-3b-2410
	[2]	ministral-3b-latest
	[3]	ministral-8b-2410
	[4]	ministral-8b-latest
	[5]	open-mistral-7b
	[6]	mistral-tiny
	[7]	mistral-tiny-2312
	[8]	open-mistral-nemo
	[9]	open-mistral-nemo-2407
	[10]	mistral-tiny-2407
	[11]	mistral-tiny-latest
	[12]	open-mixtral-8x7b
	[13]	mistral-small
	[14]	mistral-small-2312
	[15]	open-mixtral-8x22b
	[16]	open-mixtral-8x22b-2404
	[17]	mistral-small-2402
	[18]	mistral-small-2409
	[19]	mistral-small-latest
	[20]	mistral-medium-2312
	[21]	mistral-medium
	[22]	mistral-medium-latest
	[23]	mistral-large-2402
	[24]	mistral-large-2407
	[25]	mistral-large-2411
	[26]	mistral-large-latest
	[27]	pixtral-large-2411
	[28]	pixtral-large-latest
	[29]	codestral-2405
	[30]	codestral-latest
	[31]	codestral-mamba-2407
	[32]	open-codestral-mamba
	[33]	codestral-mamba-latest
	[34]	pixtral-12b-2409
	[35]	pixtral-12b
	[36]	pixtral-12b-latest
	[37]	mistral-embed
	[38]	mistral-moderation-2411
	[39]	mistral-moderation-latest

[Default]

Enter the index the name of your default model (leave empty to skip): 18
Enter model context length (leave empty to skip):
```

### Step 5: Download Patterns

Finally, download the patterns required for Fabric to function.

```bash
[Plugin Number] Enter the number of the plugin to setup (leave empty to skip): 11
```

Enter the default Git repository URL for the patterns and the folder where they are stored.

```bash
[Patterns Loader]
Enter the default Git repository URL for the patterns (leave empty for 'https://github.com/danielmiessler/fabric.git' or type 'reset' to remove the value):
Enter the default folder in the Git repository where patterns are stored (leave empty for 'patterns' or type 'reset' to remove the value):
```

## Helpers

### Step 6: Install Required Tools

Install the necessary tools and set up clipboard aliases.

```bash
$ sudo dnf install golang-bin
$ go install github.com/danielmiessler/fabric/plugins/tools/to_pdf@latest
$ sudo dnf install -y xclip xsel
```

Add the following aliases to your `.bashrc` file:

```bash
alias pbcopy='xsel --clipboard --input'
alias pbpaste='xclip -selection clipboard -o'
```

# Conclusion

Fabric is now installed and configured to be used to leverage the power of the command-line interface.