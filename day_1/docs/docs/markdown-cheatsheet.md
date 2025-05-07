📘 Markdown Cheatsheet
This cheatsheet is a quick reference to help you write rich and well-structured Markdown documents such as READMEs, logs, and design docs.

🔹 Headings
Use # for titles and section headers.

shell
Copy code
# H1 Title  
## H2 Subtitle  
### H3 Section  


🔹 Bold, Italic, Strikethrough
scss
Copy code
**Bold text**  
*Italic text*  
 
🔹 Lists
Unordered list:

markdown
Copy code
- Item 1  
- Item 2  
  - Subitem 2.1  
Ordered list:

markdown
Copy code
1. First  
2. Second  
   1. Sub-second  


🔹 Links
less
Copy code
[OpenAI](https://openai.com) 


🔹 Images
pgsql
Copy code
![Alt text]  ![Example Diagram](img/diagram.png)



🔹 Code
Inline code:

bash
Copy code
Use the `print()` function.  
Code block:

<pre> ```python def greet(name): return f"Hello, {name}!" ``` </pre>
🔹 Tables
pgsql
Copy code
| Name   | Role     | Status   |
|--------|----------|----------|
| Sejal  | Developer| Active   |
| Arun   | Tester   | Inactive |


🔹 Blockquotes
csharp
Copy code
> This is a quoted message.  


🔹 Horizontal Line
yaml
Copy code
---

🔹 Task Lists
css
Copy code
- [x] Step 1 complete  
- [ ] Step 2 pending  


🔹 Mermaid Diagrams (used for flowcharts)
<pre> ```mermaid sequenceDiagram User->>Frontend: Login Request Frontend->>Backend: Send Credentials Backend->>Database: Query User Database-->>Backend: User Found Backend-->>Frontend: Token Issued Frontend-->>User: Welcome Message ``` </pre>


✅ Use This Cheatsheet When:
Writing a README.md

Creating a daily log or journal

Documenting architecture or flows

Writing internal or open-source documentation