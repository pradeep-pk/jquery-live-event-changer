# jQuery Live to On Plugin
This is a simple Python script that replaces all instances of .live() events in your jQuery codebase with their equivalent .on() events bound to document.

How to use
Clone this repository using git clone https://github.com/pradeep-pk/jquery-live-event-changer.git
Ensure that you have Python 3 installed on your system.
Run the script using  python jquery_live_event_changer.py 'path/to/replace/live/events'
The script will modify the jQuery file in place and replace all instances of .live() with $(document).on().
Why use this script?
The .live() method in jQuery is now deprecated and has been removed from version 3.0 onwards. It was replaced with the .on() method which is more versatile and efficient. However, .on() requires an additional argument specifying the event delegation target, which can lead to confusion and errors.

This script helps you easily transition your codebase from .live() to .on() without having to modify every instance manually. It binds all events to the document object, which is a suitable delegation target for most use cases.

License
This script is licensed under the MIT License. Feel free to use and modify it as you see fit.
