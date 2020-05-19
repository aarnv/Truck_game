command = ""
while command != "quit":
    command =input("Command: ").lower()
    if command == "start":
        print("""
                            ____________________________________________
                           /|                                          |
                          / |                                          |                                
                         /  |                                          |
                        /___|                                          |                                             
           ____________/                                               |
           |                                                           | 
           |            ______                      ______             |
           |           /      \                    /      \            |
           |__________/        \__________________/        \___________|___________TRUCK STARTED
        """)
    elif command == "stop":
        print("""
                            ____________________________________________
                           /|                                          |
                          / |                                          |                                
                         /  |                                          |
                        /___|                                          |                                             
           ____________/                                               |
           |                                                           | 
           |            ______                      ______             |
           |           /      \                    /      \            |
           |__________/        \__________________/        \___________|___________TRUCK STOPPED
        """)

    elif command == "help":
        print("""
        start - car will start
        stop - car will stop
        quit - quit the game
        """)
    else:
        print("""
                            ____________________________________________
                           /|                                          |
                          / |                                          |                                
                         /  |                                          |
                        /___|                                          |                                             
           ____________/                                               |
           |                                                           | 
           |            ______                      ______             |
           |           /      \                    /      \            |
           |__________/        \__________________/        \___________|  THERE IS A PROBLEM IN THE TRUCK's ENGINE:( 
                                                                        PLS RESTART THE GAME
        """)
