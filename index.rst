=============
Shot Manager
=============
:Date: December 3rd, 2019
:Version: 0.5.8
.. contents:: 

Getting Started
---------------
Shot Manager is an add-on for Blender 2.8 and above. Created as a  tool by myself Pablo TochezA. [contact@pablotochez.com]  in order assist in the organization of complex files containing multiple shots, view layers and cameras. I am an artist with some coding knowledge for making  time saving tools and digital artworks.
Shot Manager should be installed like any .zip add-on [Blender 2.8 Install Add-ons 00:38-https://youtu.be/14G_YIVdBd0?t=38]. **Make sure you remove any previously installed versions first.** You will not loose shot data un-installing the addon/


Creating A Shot
---------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/makeshots.JPG
The main interface is found in the Properties panel under the Output tab. 

* **Enable**. The first tick box will toggle the affect of Shot Manager on you scene. Un-tick if you need to turn off its influence, particularly if rendering alternative frame ranges or View Layers.
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
* **Frame Offset** if the start or end frame is liked to a marker, you can offset frames from the linked marker position.
* **Shot Name**, A unique name for your shot, this will also be an output sub-directory and filename for the shot.(Best practice is to avoid spaces)
* **Notes**, for shot descriptions.
* **Camera object**, automatically set as render camera when shot is selected. Arrow button, select as active object.
* **Primary Layer**, select a View Layer that will become activated when selecting the shot. **Note:** If the view layer is re-named you will loose this data.
* **Transparent Background**, set film transparency for the shot.
* **View Layers**,these are the view layers that can be have their name and 'state'(Render/Non-renderable) set for the specific shot. **Clear** will empty your saved states.



Settings
--------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/settings.JPG
* **Switch to Primary**, make primary layer the active view layer when choosing shots.
* **Keep in range**, view timeline to playhead when choosing shots.
* **Unsaved layers default**,None, On and Off. The default state of view layers if they have no saved state for the active shot. Choose Off to prevent unsaved view layers from rendering. 

Output Summary
--------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Output.JPG

Scene, Root path, View Layers and other important output setting useful for checking before renders. These settings are not necessarily shot specific.
The **Root Folder** will be the starting directory for shots. Shot names are appended onto this path in subfolders.
The displayed 'RENDER PATH' shows the absolute path Blender will render to for the main output.
View Layers represent their actual render state and not their saved state. Use the small gear, button to reveal and modify their pass information without needing to change the active View Layer. 

Data
----
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/data.JPG

**Export JSON**, Export shot data to json to backup or transfer shots. 

**Import JSON**,Import shot data from a saved json file. Missing linked frame markers will be converted to manual frame ranges.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Import.JPG

**Ignore existing** to only import shots with names that don't match your scenes existing shots.
**Delete All Shots**, will clear all your saved shots.

Batch Output
------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Queue.JPG

Only queued shots will be exported. Export formats currently include fbx, obj, abc(Alembic), dae(Collada), .blend as well as .bat(Windows) files for command line rendering, either as separate files or single batch file.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Batch.JPG

Choose output format and setting in the directory window. The settings panel appears on the left in Blender 2.80.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/batch2.JPG


Compositor Nodes
----------------

Shot List Node
==============
**IMPORTANT!** for compositor nodes to have any effect, compositor 'Use Nodes' must be enabled. Node groups containing Shot Manager nodes are currently unsupported.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/ShotlistNode.JPG

The Shot List node is central to the Shot Manager nodes and is required for Constructor nodes and Multi-Switches. **A maximum of one shot list node should exist.**

**Path:** The displayed path is the projects output directory. The target folder and filenames are automatically named after the active shot. File paths are converted to absolute paths. If the Constructor nodes aren't connected to the Path Format socket, the path consists of; Root directory + shot name(folder)+ shot name + '_'(filename). However the scene render path in Blender's output settings will vary when 'Separate Layers' is active. 

**Make Multi-Switch** will create a new node group dynamically linked to active shots.

**Refresh**, non-essential node update. Although shot Manager nodes are updated upon shot change, setting or property changes, changes outside of Shot Manager won't be reflected immediately. For example adding new light passes to a View Layer. Shot Manager will update before any rendering. 

**Sync Output Paths**. Only Available if Separate Layers is disabled. Output nodes created by the user are updated so their base path matches the output path set by the Shot List node and the active shot.

**Shot List and saved states**. Here you can select and queue shots for bath export. Each shot displays the saved states for View Layers. These states can be toggled (renderable/non-renderable), removed or added. 

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/remap.JPG

**? Missing** ,Deleted or re-named shots will be displayed as red. Choose how you would like to remap the saved slot by removing or associating with an unsaved view layer.

**Path Format**. String input socket for path 'Constuctor' nodes.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/ShotlistNode2.JPG

**Separate View Layers**
Automatically generate noes to output view layers for external compositing. NOTE: nodes are generated upon any update made within the add-on, therefore generated nodes should not be directly edited. Output files will be named according to the layer name.  **You May want to delete the Composite node** when seperating layers.

**Separate Passes**
Optionally separate view layer light passes. The scene render output will match the first created ouput socket (typically 'Image') to avoid writing extra frames output from the Composite node.
**Exclude** passes from being output, not case sensitive.


Path Constructor Node
=====================

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Path%20Contructor.JPG

Use Path Contructor Nodes to create you own render path format, followed by the shot name. Connect to the Shot List 'Path Format' socket. Options; 

* Root Folder, the same folder set in the main panel. Must only be used as the first linked node.
* .Blend File, add the Blender filename to the path. Useful for iterations.
* Scene, scene name
* Shot Name
* Camera, render camera name
* Custom, enter a custom name.(Best practice is to avoid spaces)


Collections Inspector Node
==========================
Coming soon

Multi-Switch
============
Coming soon

Pandora Integration(Windows)
----------------------------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Pandora.JPG

Pandora is a free open source render ditribution software developed by Richard Frangenberg https://prism-pipeline.com/pandora/ .
Shot Manager provides a Blender specific submitter that reads the correct frame range, shot name, camera and render settings from your shot. Pandora requires at least one Coordinator enabled PC and one Slave PC in its network.

**Submitting a Shot**

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/PSubmitter.JPG

Queue a single shot by activating it and choosing 'Submit Shot'. Submit mutliple shots by enabling them in the shot list and choose 'Batch Submit Shots'. Job name and project name are required. Jobs names will be replaced with shot name when batch submitting. Pandora will save a copy of the project and queue jobs in Pandora Handler. 

**Trouble Shooting**. Pandora Core has an issue where it will often lose track of components; Coordinator.exe and Slave.exe. Therefore, the status shown in the panel might not match the actual states of these processes. This occurs especially when a process has been closed or crashed, outside of control from its settings component. Use 'Reset Pandora' to clear Coordinator and Slave states on the local machine. Make sure to close those processes(.exe) if already running, otherwise you might launch duplicate processes.


Known Issues
------------
**Pandora Submitter**. 'Cannot read json file' error may occur, has no impact on the render.

**Missing file explorer options** . This can occur when going between versions of Blender. SOLUTION- Restart Blender , disable 'Load UI' first when opening. 

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Load%20ui.JPG 



