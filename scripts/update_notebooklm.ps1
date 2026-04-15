# update_notebooklm.ps1
# Checks if nlm-sources/ changed after git pull.
# If yes - opens Claude Code to update NotebookLM sources.

$vault = "C:\Users\shemc\myVSCodeProjects\MyObsidian"
$logFile = "$vault\scripts\update_nlm.log"

function Log($msg) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$ts  $msg" | Tee-Object -FilePath $logFile -Append
}

Set-Location $vault

Log "=== Starting NLM update check ==="

# Save current HEAD
$before = git rev-parse HEAD

# Pull latest
git pull --quiet
$after = git rev-parse HEAD

if ($before -eq $after) {
    Log "No new commits. Skipping."
    exit 0
}

# Check if nlm-sources/ changed
$changed = git diff --name-only $before $after
$nlmChanged = $changed | Where-Object { $_ -like "nlm-sources/*" }

if (-not $nlmChanged) {
    Log "No nlm-sources changes. Skipping NotebookLM update."
    exit 0
}

Log "nlm-sources changed: $($nlmChanged -join ', ')"
Log "Launching Claude Code to update NotebookLM..."

# Run Claude Code non-interactively to update NotebookLM
$prompt = @"
Update NotebookLM notebook (https://notebooklm.google.com/notebook/6ffba216-e1b7-458a-9c4c-09783b1561dc):
1. For each file in nlm-sources/ (networking.txt, pentesting.txt, java_spring.txt, linux.txt, other.txt):
   - Delete the old source with the same name in NotebookLM
   - Upload the new file from C:\Users\shemc\myVSCodeProjects\MyObsidian\nlm-sources\
2. Confirm all 5 sources are updated.
Use mcp playwright browser tools to do this.
"@

claude --print "$prompt" 2>&1 | Tee-Object -FilePath $logFile -Append
Log "=== Done ==="
