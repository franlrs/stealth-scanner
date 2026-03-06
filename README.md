
# Stealth Port Scanner

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Network](https://img.shields.io/badge/Security-Red_Team-8B0000?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Read this in [English](#-english) | Leer en [Español](#-español)*

---

## 🇬🇧 English

A high-performance, containerized **TCP SYN Port Scanner** built with Python and Scapy. This tool provides fast network reconnaissance without completing the TCP handshake, preventing the scan from being registered in standard application logs.

### 💡 The Theory: TCP Connect vs. Stealth Scan

To understand how this scanner works, we must look at the standard TCP communication protocol.

When a regular application connects to a server, it performs a **3-way handshake**. Once completed, the server logs the connection. A **Stealth Scan (SYN Scan)** manipulates this process by abruptly terminating the communication before the handshake finishes.

```mermaid
sequenceDiagram
    box rgb(40, 40, 40) Standard TCP Connection (Logged)
    participant C1 as Client
    participant S1 as Server
    C1->>S1: SYN (Can I connect?)
    S1-->>C1: SYN-ACK (Yes, acknowledge)
    C1->>S1: ACK (Connection established)
    Note over S1: Connection logged by application
    end

    box rgb(30, 50, 60) Stealth SYN Scan (Unlogged)
    participant C2 as Scanner
    participant S2 as Server
    C2->>S2: SYN (Port Open?)
    S2-->>C2: SYN-ACK (Yes, acknowledge)
    C2->>S2: RST (Reset connection!)
    Note over S2: Connection dropped.<br/>No log is generated.
    end

```

### 🛠️ Core Features

| Feature | Description |
| --- | --- |
| **Speed** | Uses `concurrent.futures` to launch 100 simultaneous workers, scanning large port ranges in seconds. |
| **Stealth** | Bypasses basic firewall tracking by generating randomized source ports for every packet. |
| **Clean** | Fully containerized via Docker. It requires zero host-level dependencies (like `libpcap`), keeping your main OS untouched. |

### 🚀 Installation & Usage

1. **Clone the repository:**

```bash
git clone [https://github.com/franlrs/stealth-scanner.git](https://github.com/franlrs/stealth-scanner.git)
cd stealth-scanner
```

2. **Configure the target:**
Modify the `TARGET_IP` environment variable in `docker-compose.yaml`.

```yaml
    environment:
      - TARGET_IP=10.9.128.1
```

3. **Execute the scan:**
Run the following command. The `--rm` flag ensures the container is completely removed from your system once the scan finishes.

```bash
docker compose run --rm stealth-scanner
```

---

## 🇪🇸 Español

Un escáner de puertos **TCP SYN** de alto rendimiento y contenerizado, desarrollado en Python. Esta herramienta permite realizar reconocimiento de redes sin completar el protocolo de enlace (handshake) TCP, evitando que el escaneo quede registrado en los logs de los servidores objetivo.

### 💡 La Teoría: TCP Connect vs. Escaneo Sigiloso

Para entender el funcionamiento de este escáner, es necesario comprender el protocolo de comunicación TCP.

Cuando una aplicación normal se conecta a un servidor, realiza un **protocolo de enlace de 3 vías (3-way handshake)**. Una vez completado, el servidor registra la conexión. Un **Escaneo Sigiloso (SYN Scan)** manipula este proceso cortando la comunicación de forma abrupta antes de que el enlace termine.

```mermaid
sequenceDiagram
    box rgb(40, 40, 40) Standard TCP Connection (Logged)
    participant C1 as Client
    participant S1 as Server
    C1->>S1: SYN (Can I connect?)
    S1-->>C1: SYN-ACK (Yes, acknowledge)
    C1->>S1: ACK (Connection established)
    Note over S1: Connection logged by application
    end

    box rgb(30, 50, 60) Stealth SYN Scan (Unlogged)
    participant C2 as Scanner
    participant S2 as Server
    C2->>S2: SYN (Port Open?)
    S2-->>C2: SYN-ACK (Yes, acknowledge)
    C2->>S2: RST (Reset connection!)
    Note over S2: Connection dropped.<br/>No log is generated.
    end

```

*(Ver el diagrama superior para la representación visual del flujo de paquetes).*

### 🛠️ Características Principales

| Característica | Descripción |
| --- | --- |
| **Rapidez** | Utiliza `concurrent.futures` para lanzar 100 procesos simultáneos, escaneando grandes rangos de puertos en segundos. |
| **Sigiloso** | Evita el rastreo de firewalls básicos generando puertos de origen aleatorios para cada paquete. |
| **Limpio** | Totalmente contenerizado en Docker. No requiere dependencias a nivel de sistema host (como `libpcap`), manteniendo tu SO limpio. |

### 🚀 Instalación y Uso

1. **Clonar el repositorio:**

```bash
git clone [https://github.com/franlrs/stealth-scanner.git](https://github.com/franlrs/stealth-scanner.git)
cd stealth-scanner
```

2. **Configurar el objetivo:**
Modifica la variable de entorno `TARGET_IP` en el archivo `docker-compose.yaml`.

```yaml
    environment:
      - TARGET_IP=10.9.128.1
```

3. **Ejecutar el escaneo:**
Lanza el siguiente comando. El parámetro `--rm` asegura que el contenedor sea eliminado por completo de tu sistema al finalizar la ejecución.

```bash
docker compose run --rm stealth-scanner
```

---

### 📄 License

Project developed by **franlrs**. Distributed under the [MIT License](LICENSE).

