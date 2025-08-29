## Understanding HTML Headings, Paragraphs, and Void Elements

---

# 1. HTML Headings (`<h1>` to `<h6>`)

Headings are used for titles and subtitles in a webpage. They go from `<h1>` (biggest/most important) to `<h6>` (smallest/least important).
    `<h1>` is usually the main title of the page.  

You should only use one `<h1>` per page for clarity and SEO.

**Example:**
    
    <h1>Main Title of the Page</h1>
    <h2>Section Heading</h2>
    <h3>Subsection Heading</h3>
    <h4>Smaller Heading</h4>
    <h5>Even Smaller</h5>
    <h6>Tiny Heading</h6>

---

# 2. Paragraph (<p>) Element

The <p> element is used to write paragraphs of text. Browsers automatically add some spacing above and below each paragraph, making them easier to read.

**Example:**

    <p>This is my first paragraph in HTML.</p>
    <p>Here is another paragraph with more text.</p>


-> **Tip:** Use <p> for body text, descriptions, or any normal sentences.

---

# 3. Void Elements (Self-Closing Tags)

Some elements don’t hold any text/content inside them. They are called void elements or self-closing tags. They don’t 
    need a closing tag (</tag>).

**Common Void Elements:**

    <br>   <!-- Adds a line break -->

    <hr>   <!-- Inserts a horizontal line -->

    <img src="image.jpg" alt="Example">  <!-- Displays an image -->

    <input type="text" placeholder="Enter text"> <!-- Creates an input box -->