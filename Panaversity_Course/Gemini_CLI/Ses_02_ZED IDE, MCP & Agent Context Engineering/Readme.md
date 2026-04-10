- You can use **`ZED`** IDE to use gemini, claude and codex all CLIs on one place.

**GEMINI CLI**
* When you write prompt in gemini CLIs, what detail/data have been send along with your prompt
  1) System Instruction
  2) Tools (Default)
  3) Gemini.md files (global, as well as local you made in current folder)

* When we used Gemini in our projects, whatever work we have done yet is following the default configuration of Gemini, but we can change that default configuration like we want Gemini to use plan.md file as well or any other file, we have option for it.
  - We need to make special folder in the root and make a special file in it. Gemini CLI will follow it as well
  - Folder name should be `.gemini` and file name should be `settings.json`
  - We can add rules in this file

* We can also make GEMINI.md file within any folder in order to give context and instruction of that specific folder, in this case feature/GEMINI.md
* All files including plan.md will be loaded in this pattern:
  - First, `plan.md`
  - Then global `GEMINI.md`
  - Then current folder `GEMINI.md`
  - Then current folder/inner folder (features in this case) `GEMINI.md`
* You can also write UI/theme detail in `setting.json` file here, if you see settings.json file also present in root folder on global level, in my case it is present in C:**\Users\MyPCName\.gemini\settings.json**, when you make settings.json file in .gemini folder in your project, it will overwrite global settings.json file.

**MCP Servers with GEMINI CLI**

```json
{
  "mcpServers": {
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "GITHUB_TOKEN_MCP"
      }
    }
  }
}
```
