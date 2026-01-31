# 📌 Representation of Expressions in Programming
===============================================

In programming and computer science, expressions define computations involving operands and operators.  
Based on the **position of the operator**, expressions can be represented in three different notations:

- **Infix Notation**
- **Prefix Notation**
- **Postfix Notation**

These representations play a crucial role in **data structures**, **expression evaluation**, and **compiler design**.

---

## 🔢 Types of Expression Notation

### 1️⃣ Infix Expression
In **infix notation**, the operator is placed **between operands**.

                operand operator operand


**Examples:**


A + B
A + (B * C)
(A + B) * C


**Characteristics:**
- Most human-readable form
- Requires parentheses and operator precedence rules
- Difficult for machines to evaluate directly

---

### 2️⃣ Prefix Expression (Polish Notation)
In **prefix notation**, the operator is placed **before operands**.

operator operand operand

**Examples:**
A B

A * B C

A B C

**Characteristics:**
- No need for parentheses
- Evaluated from **right to left**
- Used internally by compilers

---

### 3️⃣ Postfix Expression (Reverse Polish Notation)
In **postfix notation**, the operator is placed **after operands**.

operand operand operator


**Examples:**
A B +
A B C * +
A B + C *
 

**Characteristics:**
- No parentheses required
- Evaluated from **left to right**
- Very easy to evaluate using a **stack**

---

## 🔄 Expression Comparison Table

| Infix Expression | Prefix Expression | Postfix Expression |
|------------------|------------------|-------------------|
| `A + B`          | `+ A B`          | `A B +`           |
| `A + (B * C)`    | `+ A * B C`      | `A B C * +`       |
| `(A + B) * C`    | `* + A B C`      | `A B + C *`       |

---

## ⚙️ Operator Precedence

| Operator | Description       | Precedence |
|---------|------------------|------------|
| `^`     | Exponent         | Highest    |
| `* /`   | Multiplication / Division | Medium |
| `+ -`   | Addition / Subtraction   | Lowest |

---

## 🔁 Steps to Convert Infix Expression to Postfix Expression
------------------------------------------------------------

1. If the symbol is an **operand**, print it immediately.
2. If the stack is empty or the top contains `(`, push the incoming operator.
3. If the incoming symbol is `(`, push it onto the stack.
4. If the incoming symbol is `)`:
   - Pop operators from the stack
   - Append them to the output
   - Stop when `(` is encountered
5. If the precedence of the incoming operator is **greater than or equal to** the operator on the stack top, push it.
6. If the precedence of the incoming operator is **less than** the operator on the stack top:
   - Pop the stack operator
   - Append it to output
   - Repeat comparison
7. After scanning the entire expression, pop all remaining operators from the stack and append them to the output.

---

## 🔁 Steps to Convert Infix Expression to Prefix Expression
-----------------------------------------------------------

1. Reverse the given infix expression.
2. Replace `(` with `)` and `)` with `(`.
3. Convert the modified expression from **infix to postfix**.
4. Reverse the postfix expression to obtain the **prefix expression**.

---

## 🧮 Expression Evaluation Using Stack

### Postfix Expression Evaluation
1. Scan expression from **left to right**
2. Push operands onto the stack
3. When an operator is encountered:
   - Pop two operands
   - Apply the operator
   - Push the result back

**Example:**
Postfix: 2 3 4 * +
Result: 14

 
---

### Prefix Expression Evaluation
1. Scan expression from **right to left**
2. Push operands onto the stack
3. When an operator is encountered:
   - Pop two operands
   - Apply the operator
   - Push the result back

---

## 🧠 Why Prefix and Postfix Are Important
- Eliminate ambiguity caused by parentheses
- Simplify expression evaluation
- Direct application of **stack data structure**
- Core concept in **compiler design**
- Efficient for machine-level computation

---

## ⚠️ Common Mistakes
- Ignoring operator precedence
- Incorrect order of popping operands
- Confusing prefix with postfix scanning direction
- Forgetting to empty the stack at the end

---

## 📚 Applications
- Expression evaluators
- Compiler and interpreter design
- Calculator implementations
- Syntax tree construction
- Stack-based algorithms

---

## 📌 Conclusion
Understanding **infix, prefix, and postfix expressions** is fundamental for mastering **data structures**, especially **stacks**.  
Prefix and postfix notations allow machines to evaluate expressions efficiently without parentheses or ambiguity.

---

## 📜 License
This README is free to use, modify, and distribute for educational and academic purposes.