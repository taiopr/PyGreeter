# Project Claude API in Python
This project provides a Python base to integrate the API of Claude, allowing to create conversations with context, answer streaming and use of tools in an easy and scalable way.

## Description
The solution is designed for developers that want to work with Claude in a structured way, inluding good practicies of configuration, example of usage and testing. It allows the creation of chats, realtime workflows and more advanced systems based on LLMs.


## Main Characteristics

- Integration of the API with Claude
- Handling conversations in context
- Real-time streaming of responses
- Tool use support
- Error handling and configuration by environment variables

## Requirements

- Python 3.8 or superior  
- pip  
- Anthropic API Key  

##  Basic Setup

1. Create and activate a virtual environment 
2. Install dependencies with `pip install -r requirements.txt`  
3. Configurate the variable `ANTHROPIC_API_KEY` inside an `.env` file.

## Usage

El proyecto incluye ejemplos simples y avanzados para:
- Enviar mensajes a Claude
- Recibir respuestas en tiempo real
- Implementar flujos conversacionales y herramientas

## 📁 Estructura

La estructura separa el código fuente, ejemplos y pruebas, facilitando el mantenimiento y la extensión del proyecto.

## 🧪 Testing

Incluye pruebas unitarias con `pytest` para validar el correcto funcionamiento del cliente y la lógica principal.

## 🛠️ Tecnologías

- Python  
- Anthropic SDK  
- python-dotenv  
- pytest  

## 📄 Licencia

Proyecto bajo licencia MIT.
