
tell application "Finder"
	
	try
		set mainDisplayPicture to "/tmp/himawariBG.png"

		tell application "System Events"
			set theDesktops to a reference to every desktop

			if((count theDesktops) > 1) then
				repeat with x from 2 to (count theDesktops)

					set picture of item x of the theDesktops to my mainDisplayPicture

				end repeat
			end if
		end tell

		set desktop picture to mainDisplayPicture

	end try
end tell