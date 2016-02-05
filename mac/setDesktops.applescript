
tell application "Finder"
	
	try
		set mainDisplayPicture to POSIX file "/tmp/himawariBG.png"
		set desktop picture to my mainDisplayPicture

		tell application "System Events"
			set theDesktops to a reference to every desktop

			if((count theDesktops) > 1) then
				repeat with x from 2 to (count theDesktops)

					set picture of item x of the theDesktops to mainDisplayPicture

				end repeat
			end if

		end tell
	end try
end tell