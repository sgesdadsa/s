# Instalação Rápida - Windows

## Problema: "myllm não é reconhecido"

Você está vendo este erro:
```
'myllm' não é reconhecido como um comando interno ou externo
```

## ✅ Solução Rápida (3 opções):

---

### **Opção 1: Usar python -m (MAIS RÁPIDO)**

Ao invés de `myllm`, use `python -m myllm.cli`:

```cmd
# Listar modelos
python -m myllm.cli ls

# Carregar modelo
python -m myllm.cli load gpt-oss-20b

# Chat
python -m myllm.cli chat

# Configuração
python -m myllm.cli config show

# Servidor
python -m myllm.cli server start
```

**Pronto! Já funciona assim!**

---

### **Opção 2: Criar atalho myllm.bat (RECOMENDADO)**

1. Copie o arquivo `myllm.bat` para `C:\Windows\` (ou outra pasta no PATH)

2. Agora você pode usar apenas `myllm`:
```cmd
myllm ls
myllm load modelo
myllm chat
```

**Arquivo myllm.bat:**
```batch
@echo off
python -m myllm.cli %*
```

**Como fazer:**
```cmd
# Opção A: Copiar para Windows (requer admin)
copy myllm.bat C:\Windows\

# Opção B: Adicionar pasta atual ao PATH
# (ver instruções abaixo)
```

---

### **Opção 3: Adicionar ao PATH**

1. Copie o caminho completo da pasta myllm-cli
   Exemplo: `C:\myllm-cli`

2. Adicione ao PATH:
   - Pressione `Win + R`
   - Digite: `sysdm.cpl`
   - Aba "Avançado"
   - "Variáveis de Ambiente"
   - Em "Variáveis do Sistema", edite "Path"
   - Clique "Novo"
   - Cole: `C:\myllm-cli`
   - OK, OK, OK

3. **Reinicie o CMD**

4. Agora funciona:
```cmd
myllm ls
myllm chat
```

---

## 📝 Instalação Completa (se ainda não instalou)

```cmd
# 1. Navegue até a pasta
cd C:\myllm-cli

# 2. Instale dependências
pip install click rich requests pyyaml tabulate fastapi uvicorn pydantic

# 3. Instale MyLLM
pip install -e .

# 4. Configure diretório de modelos
python -m myllm.cli config set models_directory "C:\seu\caminho\modelos"

# 5. Use!
python -m myllm.cli ls
```

---

## 🎯 Teste Rápido

```cmd
# Teste se funciona
python -m myllm.cli --help

# Ver configuração
python -m myllm.cli config show

# Listar modelos (se tiver .gguf na pasta)
python -m myllm.cli ls
```

---

## 💡 Dica: Criar alias no PowerShell

Se você usa PowerShell, crie um alias:

```powershell
# Adicione ao seu perfil do PowerShell
notepad $PROFILE

# Adicione esta linha:
function myllm { python -m myllm.cli $args }

# Salve e recarregue:
. $PROFILE

# Agora funciona:
myllm ls
```

---

## 🚀 Uso Diário

Depois de configurado, use assim:

```cmd
# Ver modelos disponíveis
python -m myllm.cli ls

# Configurar diretório (primeira vez)
python -m myllm.cli config set models_directory "C:\progeto\lmstudio-community"

# Carregar modelo
python -m myllm.cli load gpt-oss-20b

# Iniciar chat
python -m myllm.cli chat

# Ver modelos carregados
python -m myllm.cli ps

# Iniciar servidor API
python -m myllm.cli server start

# Verificar servidor
python -m myllm.cli server status
```

---

## ✅ Checklist

- [ ] Python instalado (`python --version`)
- [ ] Dependências instaladas (`pip list | findstr click`)
- [ ] MyLLM instalado (`pip show myllm` ou `pip list | findstr myllm`)
- [ ] Funciona com: `python -m myllm.cli --help`
- [ ] (Opcional) `myllm.bat` copiado para C:\Windows
- [ ] (Opcional) PATH configurado
- [ ] Diretório de modelos configurado
- [ ] Modelos .gguf na pasta

---

## 🆘 Ainda não funciona?

Execute o diagnóstico:

```cmd
cd C:\myllm-cli
diagnose.bat
```

Ou teste simples:

```cmd
python test_simple.py
```

---

## 📚 Documentação Completa

- `LEIA_PRIMEIRO.txt` - Começe aqui
- `TROUBLESHOOTING_WINDOWS.md` - Solução de problemas
- `WINDOWS_GUIDE.md` - Guia completo Windows
- `README.md` - Documentação completa

---

## 🎉 Resumo

**Use isso e funciona imediatamente:**

```cmd
python -m myllm.cli <comando>
```

**Para criar atalho "myllm":**

```cmd
copy myllm.bat C:\Windows\
```

Pronto! 🚀
