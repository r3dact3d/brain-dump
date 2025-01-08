```mermaid
graph TD
    A[Fabric Installation] --> B[Download Fabric]
    B --> C[Move to /home/r3dact3d/bin]
    C --> D[Verify Installation]
    D --> E[Setup Fabric]
    E --> F[Configure AI Vendors]
    F --> G[Configure Tools]
    G --> H[Download Patterns]
    H --> I[Set Up Helpers]
    I --> J[Run Example Commands]

    subgraph Install
        B
        C
        D
    end

    subgraph Setup
        E
        F
        G
        H
    end

    subgraph Helpers
        I
    end

    subgraph Examples
        J
    end

    click B "curl -L https://github.com/danielmiessler/fabric/releases/latest/download/fabric-linux-amd64 > fabric && chmod +x fabric && ./fabric --version"
    click C "cd && mkdir bin && mv fabric bin/ && fabric --help"
    click E "fabric --setup"
    click F "Enter 9 (Mistral)"
    click G "Enter 10 (Default AI Vendor and Model)"
    click H "Enter 18 (mistral-small-2409)"
    click I "sudo dnf install golang-bin && go install github.com/danielmiessler/fabric/plugins/tools/to_pdf@latest && sudo dnf install -y xclip xsel && alias pbcopy='xsel --clipboard --input' && alias pbpaste='xclip -selection clipboard -o'"
    click J "fabric -p enrich_blog_post -o /home/r3dact3d/working/foamy-stuff/dump.md --output-session -u https://r3dact3d.github.io --dry-run"
```

### VISUAL EXPLANATION

- **Fabric Installation**: The process starts with downloading and moving the Fabric binary to the user's bin directory.
- **Setup**: The setup involves configuring AI vendors and tools, including selecting the default model.
- **Helpers**: Additional tools and aliases are set up for helper functions.
- **Examples**: Example commands demonstrate how to use Fabric for enriching blog posts.
