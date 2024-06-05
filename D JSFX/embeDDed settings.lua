-- Import the required functions
reaper.ClearConsole()

-- Function to show a message box and get user input
function getOSSelection()
    local title = "embeDDed settings"
    local message = "Are you using linux?"
    local defaultChoice = 0
    
    -- Show the selection dialog with buttons
    local retval = reaper.ShowMessageBox(message, title, 3) -- 3 buttons (Yes/No/Cancel)
    
    if retval == 6 then  -- 'Yes' button clicked, assuming it's Linux
        return 1
    elseif retval == 7 then -- 'No' button clicked, assuming it's Windows/MacOS
        return 0
    else
        return nil
    end
end

-- Function to update or create the file with the correct ddconfig_os value
function updateConfigFile(ddconfig_os)
    local filePath = debug.getinfo(1, "S").source:match("@(.*[\\|/])") .. "../../Effects/D JSFX/DGFX/ddconfig_os.jsfx-inc"
    
    local file = io.open(filePath, "w")
    if file then
        file:write(string.format("<?\n    ddconfig_os=%d;\n?>", ddconfig_os))
        file:close()
        reaper.ShowMessageBox("Updated settings", "Success", 0)
    else
        reaper.ShowMessageBox("Error opening file for writing.", "Error", 0)
    end
end

-- Main script execution
local ddconfig_os = getOSSelection()
if ddconfig_os ~= nil then
    updateConfigFile(ddconfig_os)
else
    reaper.ShowMessageBox("Operation cancelled by user.", "Cancelled", 0)
end
