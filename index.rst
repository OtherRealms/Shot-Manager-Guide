=============
Shot Manager
=============
:Date: December 3rd, 2019
:Version: 0.5.6
.. contents:: 

Getting Started
---------------
Shot Manager is an addon for Blender 2.8 and above. Created as a  tool by myself Pablo TochezA. [contact@pablotochez.com]  in order assist in the organisation of complex files containing multiple shots, view layers and cameras. I am by no means a programmer but rather an artist with some basic coding knowledge for making  time saving tools and digital artworks.
Shot Manager should be intalled like any .zip addon [Blender 2.8 Install Addons 00:38-https://youtu.be/14G_YIVdBd0?t=38].


Creating A Shot
---------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/makeshots.JPG
The main interface is found in the Properties panel under the Output tab. 

* The first tick box will toggle the affect of Shot Manager on you scene. Untick if you need to turn off its influence.
* **Add new** , adds a new shot to your list.
* Arrows Up and Down  will sort your shots, but ultimately have no affect on your project.
* The Tick Box on the Left of your shot name will add it to the output/render queue.
* Click '-' to delete the shot 
* **Queue all** to add all shots to output/render queue.
To activate a shot simply select it in the list!

Shot data
---------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/specifics.JPG

Each shot contains its own data set that may include any of the following:

* **Start Frame**
* **End Frame**
* **Linked Marker** a second layer for the start/end frames are created when linking to a selected Timeline Marker
* **Frame Offset** if the start or end frame is liked to a marker, you can offset frames from the linked marker postion.
* **Shot Name**, A unique name for your shot, this will also be an output sub-directory and filename for the shot.
* **Notes**, for shot descriptions.
* **Camera object**, automatically set as render camera when shot is selected. Arrow button, select as active object.
* **Primary Layer**, select a View Layer that will become activated when selecting the shot. **Note:** If the view layer is re-named you will loose this data.
* **Transparent Background**, set film transparency for the shot.
* **View Layers**,these are the view layers that can be have their name and 'state'(Render/Non-renderable) set for the specific shot. **Clear** will empty your saved states.



Settings
--------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/specifics.JPG
* **Switch to Primary**, make primary layer the active view layer when choosing shots.
* **Keep in range**, view timeline to playhead when choosing shots.
* **Unsaved layers default**,None, On and Off. The deafault state of view layers if they have no saved state for the active shot. Choose Off to avoid unsaved view layers from rendering. 

Output Summary
-------------
Coming soon

Data
----

Batch Output
------------
Coming soon

Nodes
-----
Coming soon

Shot List Node
==============
Coming soon

Path Constructor Node
=====================

Coming soon

Collections Inspector Node
==========================
Coming soon

Multi-Switch
============
Coming soon

Pandora Integration
-------------------

