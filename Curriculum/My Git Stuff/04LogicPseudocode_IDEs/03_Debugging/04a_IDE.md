
# Using an IDE

For this lesson, we are going to dive into using IDEs to debug. The IDEs we will be using are **CLion** and **Visual Studio**. Both are outstanding and powerful debuggers. 

![](/assets/clion.png)

* **License:** Proprietary
* **Platforms:** Windows, OSX, Linux
* **Price:** $89 1st year (monthly payments and free/dicounted accounts avaliable)
* Truly cross-platform (full functionality on all platforms)
* Intelligent autocompletion engine
* Utilizes CMake and other system tools for building
* Can use LLVM (Clang) or GCC compiler
* Easy to setup
* Powerful refactoring
* Faster than Intellisense
* Large amount of plugins
* Powerful debugger
* Code analysis
* We will be using this on Linux

![](/assets/vs.png)

* **License:** Proprietary
* **Platforms:** Windows, OSX, Linux (limited functionality on OSX/Linux)
* **Price:** Paid/Free (Community version is free)
* Intellisense (Very powerful auto completion, peaking, etc)
* Good range of plugins
* Integrated well with Windows
* Pretty simple
* Ironed Out
* Utilizes MSBuild tools
* We will be using this on Windows

---
---
---

## Objectives

During this topic the student will have a fundemental understanding on IDE setup and use to include the following.
* **Why use an IDE**
* **IDE Basic Use**
* **CLion tool decsriptions**
* **Visual Studio tool descriptions**

---

## Why use an IDE?

There are many reasons to use an IDE over a text editor.  

1. Code highlighting, syntax validation, auto code formatting and auto completion. Sure, many of the above text editors have that functionality. But you can be sure the above IDEs implement that functionality much better. Especially when we are talking about projects with multiple files.
2. Debugging: This is arguably the biggest reason. Text Editors with plugins have the ability to debug... but it's rather limited. With Visual Studio and CLion... you can dive into assembly, static analysis, dynamic analysis, memory, peak, stack trace, watch values, etc. 
3. Compiling and managing lib dependencies: On large projects... you may need to set a compile order of files, manage lib dependencies, handle cleanup, etc. Sure, you can create scripts to do this. But it can become overwelming. IDEs can do it for you and save you a bunch of time. 
4. Result Preview: IDEs generally handle your final result previews better. This also includes the creation of GUIs. 
5. Refactoring and performance hints: IDEs can help you refactor code across the entire project in one or two steps. IDEs can also provide hints on how to increase the performance of your project. 
6. Inspecting Code: IDEs allow for the inspection of code as you are programming. This helps a ton when dealing with libs.
7. Documentation: IDEs often include tools to assist in documentation... even doing it for you sometimes. 
8. Team tools: IDEs include and can utilize plugins to streamline the team development process.

---

# IDE Basic Use

The first step to using an IDE, is to create a new project. We are briefly going to discribe how to do this in markdown. For a more in-depth live preview follow along with the instructors demonstration. 

## CLion

1. Open CLion
2. Click `New Project`
3. For our C Programs, choose `C Executable` using the C99 standard
4. Give your project a name, our project is called `myProject`
5. Click Create

![](/assets/clion_new.png)

You will then be presented with a window. 

Two files will have been created: `
* CMakeLists.txt`. 
  * This file is what configures CMake to make and build our project. 
* main.c file. 
  * This is our entry point for our project; at least in relation to programming in C. 

![](/assets/clion_project_window.png)

There are multiple `tool windows` within the standard CLion workspace. We are primarily going to discuss those associated with the project window. 

#### Project Window

* Contains all of our files, External Libraries, etc. 
* We are mostly interested with whats inside of the `myProject` dir. (This will be called whatever you named your project)

Expanding the , we see the cmake file, the .c file and a dir called `cmake-build-debug`. (All of the executables, debugging files, etc go here)

* [More info](https://www.jetbrains.com/help/clion/project-tool-window.html)

![](/assets/clion_window.png)

Additional options are available by right clicking `myProject` and include: 

* Click on `Directory' creates new directory's
  * This should create a link on the CMake file. If it doesn't; then manually add it. 
* To create new C sources files, click `C/C++ Source File`
  * This should create a link on the CMake file. If it doesn't; then manually add it. 
  * Ensure you select the correct language type (C)
* To create new C header files, click `C/C++ Header File`
  * This should create a link on the CMake file. If it doesn't; then manually add it. 
  * Ensure you select the correct language type (C)

![](/assets/clion_rclick.png)

#### Code Window

The code window appears as a large empty windw. It is used to write your code. 

#### Run/Debugging Bar

This bar is a quick and graphical representation of the Build and Run dropdown menus. 

* Green right arrow - runs your code. 
  * Output will be displayed in the output/terminal window which will appear below the code window. 
* Green bug - puts your program into debugging mode. 

The other buttons are useful, but we will not discuss it in the markdown.

The `build` dropdown menu will also provide some additional functionality.
    * `Rebuild Project` will rebuild your project. Even if you didn't make any changes. 
    * `Clean` will clean the project by building the clean target from the current CMake profile

[More Info](https://www.jetbrains.com/help/clion/build-actions.html)

![](/assets/run_bar.png)

#### Terminal/CMake/TODO Window

Once you run your code; the terminal window will show your output, any errors, Cmake information, and any TODOs you create.

![](/assets/clion_term.png)

* To create a TODO, you simply type `// TODO:` as a comment. 

### More Info on Getting Started with CLion

[CLion - Getting Started](https://www.jetbrains.com/help/clion/clion-quick-start-guide.html)



---
---
---

## Visual Studio

When setting up Visual Studio for coding/debugging, a few steps to be accomplished first.
* Open Visual Studio
* Click `File -> New -> Project`
* For our C Programs, choose `Visual C++` on the left side
* Click `Empty Project` in the middle window
* Give your project a name and press `OK`

![](/assets/vs_new.PNG)

---

There are multiple `tool windows` within the standard Visual Studio workspace that we need to discuss.

![](/assets/vs_main.PNG)

---

### Solution Explorer

Solution explorer is located on the right side of the screen.  It contains all of our project files:  References, external dependencies, header files, resource files, and source files.

![](/assets/vs_solutions.PNG)

Source files are created in the source directory and header files in the header directory.
**Note:** You can add new directories as you wish and place other files where you choose.

---

### Properties Window

This window contains details about an item that we clicked on in the solutions window. Details include information such as name, UID, location, etc. 

![](/assets/vs_prop.PNG)

---

### Code Window

The code window is where you create, view, and modify code

![](/assets/vs_code_win.PNG)

---

### Tool Bar

The tool bar is located just above the code window.  It contains a lot of quick to access icons. 
* New Project
* Open
* Save
* Save All
* Type of Build (debug, release, etc)
* Platform
* Build+Run button
![](/assets/vs_toolbar.PNG)
These choices are also available via kepboard shortcuts or dropdown menus.

---

### Output Window

The output window is located just below the code window. The output window displays tasks that are occuring within the build. It displays compiling errors and is used for debugging your code.

![](/assets/vs_output.PNG)

---

### Summary

During this topic, we discussed
* Why use an IDE
* IDE Basic Use
* Clion tool description
* VStudios tool description

### More Info on Getting Started with Visual Studio

* [Visual Studio - Getting Started](https://www.cs.auckland.ac.nz/~paul/C/Windows/index.php)

---
