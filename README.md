## Pong Project

"Pong is one of the earliest arcade video games and the very first sports arcade video game. It is a table tennis sports game featuring simple two-dimensional graphics." - wikipedia

This 1972 classic arcade game was the final project for the course "An Introduction to Interactive Programming in Python (Part 1)" by Rice University offered at Coursera. With this project we put in practice the principles of Event Driven Programming model where you you write a program that initalizes and just wait for an event and when it occurs, the program access a function that will handle that event 'Handler' and once it's done, the program waits.

The game was coded in Python 2 and developed on a platform called CodeSkulptor developed by the Professor Scott Rixner which allows to save the game on the browser as well as the computer and play it on any browser.

The criteria to conclude this project were:
- The ball spawns in the middle of the canvas with either an upward left or an upward right velocity. No credit if the ball moves only horizontally left or right. Bleh, that would be boring!
- The ball bounces off of the top and bottom walls correctly. (1 pt each)
- The ball respawns in the middle of the screen when it strikes the left or right gutter but not the paddles. (1 pt for each side) Give credit for this item even if the ball hits the edge of the canvas instead of the gutter.
- The left and right gutters (instead of the edges of the canvas) are properly used as the edges of the table.
- The ball spawns moving towards the player that won the last point.
- The 'w' and 's' keys correctly control the velocity of the left paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to 'w' and 's' key presses.)
- The up and down arrows keys correctly control the velocity of the right paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to up and down arrow key presses.)
- The edge of each paddle is flush with the gutter. (1 pt per paddle)
- The paddles stay on the canvas at all times. (1 pt per paddle)
- The ball correctly bounces off the left and right paddles. (1 pt per paddle)
- The scoring text is positioned and updated appropriately. The positioning need only approximate that in the video.
- The game includes a "Restart" button that resets the score and relaunches the ball.

If you want to see the code on Github:
https://github.com/bruno78/pong.git

or if you want to play the game:
http://www.codeskulptor.org/#user41_VoGZTf5hOe7otdE.py
