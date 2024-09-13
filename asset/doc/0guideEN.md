


> Written with [StackEdit](https://stackedit.io/) (I love this tool give them some love)

## **Using fNotes**

### -1. Content

 - **0.** Creating new notes
 - **1.** Selecting notes
 - **1.1** Opening notes
 - **2.** Changing the name of the note
 -  **3.** Writing your note
 - **3.1** Basic
 - **3.2** Advanced
 - **4.** Save notes
 - **4.1** Autosaves (Tmp)
 - **5.** Delete note
 - **6.** Mathematics
 - **7.** About
 -  **8.** Settings

### 0. Creating new notes
First, click on **Note** in the top-left corner of the window, then on **New** to create a completely new note. Remember that this does not save any changes made to the current note.

### 1. Selecting notes
When running fNotes for the first time you might notice two boxes with text within them. In the code they're referenced to as "listWidget" and "tmpListWidget".

As you can see by the name they're both lists that contain items. When clicking on a name in one of these boxes you are practically opening a note. The content of the note is being inserted into the editor (the big box in the lower half of the screen) and the name of it into the name-Label.

#### 1.1 Opening Notes
If a collegue or pretty much anyone sends you a fNotes file and you want to view it, click on **Note** in the top-left corner of the screen, then on **Open** and select the file you would like to open. Remember that this deletes any progress made on your current note.

### 2. Changing the name of the Note
To change the name of the current note you have to change the text in the nameLabel text line.

### 3. Writing your note
This version of fNotes features a few features to edit your note.
All functions you could use:

### 3.1 Basic:
 -  **F** >> Makes the selected text bold
 -  **U** >> Underlines the selected text
 -  **K** >> Makes the selected text italic
 - **L** >> Aligns the text to the left side of the editor
 - **M** >> Aligns the text with the center
 - **R** >> Aligns the text with the right side of the editor
 - *SpinBox* (?px) >> Changes the size of the selected text
 - **Σ** >> Solves a mathematical problem. More info on this in: 6.
 - *The (black) boxes* >> Changes either the foreground or background color of the selected text.
 - • >> Creates a bulletpoint list
 - **1.** >> Creates a list with decimal numbers
 - **a.** >> Creates a list with each letter of the alphabet
 - **IV.** >> Creates a list with roman numbers
 - **Image** >> Inserts an Image into the editor
 - **Table** >> Inserts a table into the editor

### 3.2 Advanced
- **Font weight** >> Changes the weight of the font
- **Font** >> Changes the font.

### 4. Save Notes
To save a note, press on **Note** in the top-left corner of the screen and then on **Save**. This automatically saves the note so it can be viewed next time you open the program.

#### 4.1 Autosaves (Tmp)
The program automatically saves any note you currently have open every five seconds. Those files can be viewed in the tmpListWidget (the list on the top-right). As you can maybe notice, the notes name always ends with "Tmp" so you know it's an automatic save. If you don't like being bombarded with Tmp-Notes, you can delete them. (see 5.)

### 5. Delete notes
To delete a note you first have to click on a note and then click on the "Delete current note"-button on the bottom-left. Alternatively you can delete your current note when clicking on **Note** and then on **Delete**

### 6. Mathematics
The basic calculator ( **Σ** ) can solve basic mathematical problems.
This includes:
- Square roots (sqrt) | Usage: "sqrt(2)" -> 1.414...
- Sin | Usage: "sin(2)" -> [number]
- Cos | Usage: "cos(2)" -> [number]
- log | Usage: "log(2)" -> [number]
- exp | Usage "exp(2)" -> [number]
- pow | Usage "pow(2, 3)" -> 8
	- Alternatively: 2 ^ 3 -> 8 **or** 2 ** 3 -> 8
- pi | Usage "pi" -> 3.141...

### 7. About
To open the "About" window: **Help** >> **About**.

### 8. Settings
In the **Settings** tab (**Other** >> **Settings**) you can change a few settings to match your preferences.
Settings:
- Set language of the **About** section (In v0.9 it also translates the Main Window)
- Decimal points when using the calculator (1-9) (e.g. if you change it to **5** and you try **1 / 3** you'll get 0.33333).
- Interval for Auto-Saves (something between 0 and 300 seconds. If you set it to 0 seconds the program will never automatically save. In the code it will just set the wait-time to 9,509,509 seconds lol)
- The standard Font-Size (between 1px and 128px)
- Enable/Disable word-wrap in editor
