# 🌊 .CORAL Framework Compiler / Interpreter

## 🔹 Overview

**.CORAL** is a next-gen **compiler/interpreter framework** designed to **expand and upgrade NEMOlang** and the older **GNFR (Global Novaxis Framework and Runtime)**.

Unlike traditional compilers, .CORAL does **not** output executable bytecode. Instead, it compiles programs into **Serialized Intermediate Representation (IR)** expressed as **JSON** — called **JsnButler**.

Execution is still **interpreted**, while the JSON IR is used for:

* 📦 Carrying program values
* 🧮 Representing tape and pointer states
* 🔗 Runtime interop with other languages
* 🛠️ Debugging & analysis

This makes .CORAL a **hybrid model**: **compile → IR → interpret execution.**

---

## ✨ Features

* 📝 **Template & framework** for creating new languages
* 🧵 **Serialized IR (JSON-based)** output system (JsnButler)
* 🧭 **2D tape support** (X-tape + Y-tape) with pointers
* 🛡️ **Error handling** for invalid file extensions / bad markers
* 🔍 **Debug logging** (`steps_executed`)
* ⚡ **Modular design** → easily expand with new commands
* 🔗 **Interop-friendly** for embedding into other runtimes

---

## 📂 File Extensions

Valid extensions are defined in:

```python
legalfes = [".nec", ".nemoc"]
```

⚠️ If a file does not match, a `FileNotFoundError` is raised.
➡️ Change these to whatever extensions you want your language to support.

---

## ⚙️ Execution Flow

1. 🚀 Source file must start with a **SoF marker** (e.g. `I`) and end with an **EoF marker** (e.g. `$`).
2. 🧾 Interpreter parses commands **character by character**.
3. 🔀 Depending on the command:

   * Capital → operates on **X-tape**
   * Lowercase → operates on **Y-tape**
   * Special chars → control flow, I/O, comments, math
4. 🧩 Outputs, tape states, and debug info are stored into a `.json` file.

---

## 🖥️ Example Usage

```bash
# Compile/interpret a program
python3 coralfr.py my_program.nec

# Output written to:
my_program.json
```

📄 Example JSON IR:

```json
{
  "program_name": "my_program.nec",
  "legal_file_extensions": [".nec", ".nemoc"],
  "tape": {
    "x_tape": [0,1,2],
    "y_tape": [0,0,0]
  },
  "pointers": {
    "x_pointer": 2,
    "y_pointer": 0
  },
  "outputs": ["H","i"],
  "debug": {
    "steps_executed": 128
  }
}
```

---

## 🛠️ Customization

When building your own language with .CORAL:

* 🔧 **Edit** `legalfes` for your extensions
* 📜 **Define SoF/EoF markers**
* ➕ **Add new commands** into the interpreter loop
* 📡 **Extend JSON schema** for your runtime needs

---

## 📜 License

Licensed under the **GPL 3.0 License** — free to use, modify, and expand.
Just keep the license intact when redistributing and do not close source.

---

🔥 **.CORAL isn’t just a language — it’s a framework for building languages.**
