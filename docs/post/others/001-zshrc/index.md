
<div align="center"><font size="35">zshrc笔记</font></div>

- [1：zshrc 文件](#1zshrc-文件)
- [2：其他说明](#2其他说明)

# 1：zshrc 文件

```bash
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/lucas/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes

# 修改默认主题
ZSH_THEME="ys"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
    git
    zsh-syntax-highlighting
    zsh-autosuggestions
    sudo
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# 修改默认编辑器为vim
export EDITOR=/usr/bin/vim

export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$GOPATH:$GOBIN:$GOROOT/bin:$PATH

export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup

export PATH="$HOME/bin:$HOME/.local/bin:$PATH"
export PATH="$PATH:/mnt/c/Program\ Files/Docker/Docker/resources/bin"
export PATH="$PATH:/usr/local/lib/node-v16.4.2-linux-x64/bin"

# export DOCKER_HOST="tcp://0.0.0.0:2375"

# alias
# alias docker=docker.exe
# alias docker-compose=docker-compose.exe
# alias go colorgo

# history 命令显示时间
export HIST_STAMPS="yyyy-mm-dd"

# ----------------proxy----------------------
#
WindowsIP=$(cat /etc/resolv.conf | grep -oP '(?<=nameserver\ ).*')
PROXY_PORT=7078
PROXY_HTTP="http://${WindowsIP}:${PROXY_PORT}"
# Git & SSH for Git proxy
proxy_git() {
    git config --global http.https://github.com.proxy ${PROXY_HTTP}
    if ! grep -qF "Host github.com" ~/.ssh/config; then
        echo "Host github.com" >>~/.ssh/config
        echo "  User git" >>~/.ssh/config
        echo "  ProxyCommand nc -X 5 -x ${PROXY_SOCKS5} %h %p" >>~/.ssh/config
    else
        lino=$(($(awk '/Host github.com/{print NR}' ~/.ssh/config) + 2))
        sed -i "${lino}c\  ProxyCommand nc -X 5 -x ${PROXY_SOCKS5} %h %p" ~/.ssh/config
    fi
}
# Set proxy
set_proxy() {
    export http_proxy="${PROXY_HTTP}"
    export https_proxy="${PROXY_HTTP}"
    proxy_git
}
# Unset proxy
unset_proxy() {
    unset http_proxy
    unset https_proxy
    git config --global --unset http.https://github.com.proxy
}

# Set alias
alias proxy=set_proxy
alias deproxy=unset_proxy

alias px='proxychains4' # 此后 px curl google.com

# wsl sync time
# alias synctime='sudo ntpdate asia.pool.ntp.org;sudo ntpdate time.nist.gov;'
alias synctime1='sudo ntpdate asia.pool.ntp.org;'
alias synctime2='sudo ntpdate time.nist.gov;'

# 手动释放内存
alias freemem='~/myshell/free-mem.sh'

# alias godoc='GO111MODULE=off godoc'
alias fy='unproxy dict'

```

# 2：其他说明
