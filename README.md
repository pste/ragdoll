# RAGDOLL
Building a RAG on a monolithic repo.
RAGDOLL stands for **RAG** on **DO**cker with local **LL**m (and surely recalls the Aerosmith [song](https://www.youtube.com/watch?v=mrEC8xGc3ZM))

## Setup

### Prepare the PC
I'm using Python 3.11 so let's ensure it's installed in the machine (in my case it's an Ubuntu OS):
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv
```  

Furthermore I'm using [uv](https://github.com/astral-sh/uv) as package manager, instead of `pip`. It is fast and allows us to avoid having multiple `pip` for multiple `python` versions:  
`curl -LsSf https://astral.sh/uv/install.sh | sh`

### Virtual Env
Every Python projects runs under a venv to avoid messing with local libraries. Please refer to the single project instructions for details.  
If needed you can just `rm` the `.venv` folder and restart from scratch.

### Local Dev
I'm using a local `.private/` folder that is excluded from the repo and contains env files and build/run scripts.
I'm under wsl2 so sometimes strange things happen (ie: core dump from cuda stuff as the `nvidia-smi` command); to (brutally) reset the env:
- close every VSCode
- close every wsl2 windows
- launch `wsl --shutdown` from a new windows command prompt

## Chroma DB
The vector store [documentation](chroma/README.md)

## LLM
The LLM engine store [documentation](llm/README.md)

## UI
The UI [documentation](ui/README.md)
