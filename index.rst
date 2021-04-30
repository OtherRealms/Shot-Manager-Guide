=============
Shot Manager
=============
https://twitter.com/OTrealms

:Version: 0.7.2

.. contents:: 

Getting Started
---------------
Shot Manager is an add-on for Blender 2.8 and above. Created as a  tool by myself Pablo TochezA. [contact@pablotochez.com]  in order to assist in the organization of complex files containing multiple shots, view layers and cameras. I am an artist with some coding knowledge for making time saving tools and digital artworks.
Shot Manager should be installed like any .zip add-on [Blender 2.8 Install Add-ons 00:38-https://youtu.be/14G_YIVdBd0?t=38]. **Make sure you remove any previously installed versions first.** You will not loose shot data un-installing the addon/
This documentation is intended for the paid version available on Blender Market, however features included in the lite version are included.

version 0.7 and above do not support version of Blender below 2.90.

Main vs List
============
The 'Main' shot is intended for general editing and previewing and is not considered for batch rendering or exporting. Settings can be copied to and from the Main shot and Shot List. 'List' shot defaults are inherited from the Main shot.

Creating A Shot
===============
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Makeshots.PNG
The main interface is found in the Properties panel under the Output tab.

* **Enable**. The first tick box will toggle the affect of Shot Manager on you scene. Un-tick if you need to turn off its influence, particularly if rendering alternative frame ranges or View Layers.
* **Root Folder** will be the starting directory for shots. Shot names are appended onto this path in subfolders.
* **Add new** , adds a new shot to your list.
* **Duplicate** , Duplicate active shot.
* Arrows Up and Down  will sort your shots, but ultimately have no affect on your project.
* The Tick Box on the Left of your shot name will add it to the output/render queue.
* Click '-' to delete the shot 
* **Queue all** to add all shots to output/render queue.
To activate a shot simply select it in the list!


Still Mode
==========
For rendering single frames. Works with batch render. Uses an alternative frame to the normal start and end parameters. Will output from all available output nodes.

Generate View Layers Mode
=========================
This mode enables settings; Switch to Primary Layer, Generate Primary Layers and Unsaved View Layers Default to 'Primary Layer'.
The workflow is designed for users who wish to create unique View Layers with each shot, so as to have different collection visible. This workflow is most commonly used in product rendering and visualisation. The newly created view layer will be set as the layer's Primary layer. The prmimary layer in combination with the other settings mentioned, will become the active View Layer and default as renderable when the shot is selected. It is therefore not neccessary to alter the View Layer save/render states for the shot.

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
* **Render Engine**, set render engine for specifiaclly for the shot, now supports addon engines.
* **Render Samples**, If using Render Engine override. Override samples, 0 = no overide.
* **World** , World data, inherits from Main if empty.
* **Primary Layer**, select a View Layer that will become activated when selecting the shot. **Note:** If the view layer is re-named you will loose this data.
* **View Layers**,these are the view layers that can be have their name and 'state'(Render/Non-renderable) set for the specific shot. **Clear** will empty your saved states.
* **Transparent Background**, set film transparency for the shot.
* **Overide Resolution** , shot specific output resolution.
* **Bloom**, Eevee only.
* **View Layers**, View layers states (unsaved/renderable/not-renderable),'AB' icon means: Rename the Primary Layer to match the shot's name. 'Broken Link' icon means: the shot has an identical name to this View Layer, set as Primary.
* **Material Overrides**, toggle use of collection overrides.


Collection Overrides
====================
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/overrides.JPG
Ensure that the Collection Overrides property is enabled. Only first level view layer collections are available.
Currently material overrides are available per collection, per shot. Add and override and select collection, then add a material and slot. Override data is stored in the collections not shots, therefore can't be exported as a Json file or copied from another shot.
Also editable in the Collections Inspector Node including overrides for all shots.
Using overrides may be slower when switching shots and there are large amounts of collections and objects.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/material_override.JPG
The orginal material can be restored using the revert button foun in the objects material tab. Useful if an object has been moved out of a collection and you want to restore its pre-override material. 


Settings
--------
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/settings.JPG
* **Switch to Primary**, make primary layer the active view layer when choosing shots.
* **Generate Primary Layers**, a new View Layer will be created with the name of the newly made shot and associated as a Primary Layer
* **Keep in range**, view timeline to playhead when choosing shots.
* **Jump to First Frame**, place playhead at start of frame range when choosing shots.
* **Unsaved layers default**,On,Off, Primary Layer and None. The default state of view layers if they have no saved state for the active shot. 'On' will make all unsaved layers renderable by default with each shot change/trigger. 'Off' will default to un-renderable, choose 'Off' to prevent unsaved view layers from rendering.'Primary Layer' will also switch all unsaved layers to un-renderable, except for the Shot's Primary Layer. 'None' leaves the current states, no influence form the add-on. 
* **Seperator** , a custom seperator to add between filenames and frame suffix, default is '_'
* **Path Type** , Absolute or relative output path creation.

Data
====
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/data.JPG

**Export JSON**, Export shot data to json to backup or transfer shots. Does not include collection overrides.
**Include Shot Manager Settings**, include settings from settings panel.

**Import JSON**,Import shot data from a saved json file. Missing linked frame markers will be converted to manual frame ranges.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Import.JPG

**Ignore existing** to only import shots with names that don't match your scenes existing shots.
**Delete All Shots**, will clear all your saved shots.

Shot Manager Output
-------------------
Shots can be rendered using the regular render animations or still operators (ctr+F12/F12). However only the active shot will be rendered. To bect render simply use ctr+shift+F12.


Output Summary
==============
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/summary.JPG

Scene, Render path, View Layers and other important output setting useful for checking before renders. These settings are not necessarily shot specific.
The displayed 'RENDER PATH' shows the absolute path Blender will render to for the main output.
View Layers represent their actual render state and not their saved state. Use the small gear, button to reveal and modify their pass information without needing to change the active View Layer. 



Batch Output
============

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Queue.JPG

Only queued shots will be exported. Export formats currently include fbx, obj, abc(Alembic), dae(Collada), .blend as well as .bat(Windows) files for command line rendering, either as separate files or single batch file. 

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Batch.JPG

Choose output format and setting in the directory window. The settings panel appears on the left in Blender 2.80.

FBX exporter does not use the FBX export/import addon but rather a modified export script.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/embed_shots_a.JPG

Embedded shots can store frame ranges and shot names as animation layers and extracted in other software,ie Unity.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/embed_shots_b.JPG

**Batch Render Shots** ,Render all queued/enabled shots.

**Internal Shot List**, Render shots from the currently open Blend file(Less memory efficient than external).  

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/batch%20renderB.JPG

**External Blend** , Open a shotlist from an external Blend file(uses the files active scene). Shots can be queued once loaded.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/batch%20renderA.JPG


Pandora Integration 1.1.0.8(Windows)
====================================
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Pandora.JPG
Tutorial and trouble shooting: https://youtu.be/LgR-uqd4h9o

Pandora is a free open source render ditribution software developed by Richard Frangenberg https://prism-pipeline.com/pandora/ .
Shot Manager provides a Blender specific submitter that reads the correct frame range, shot name, camera and render settings from your shot. Pandora requires at least one Coordinator enabled PC and one Slave PC in its network.

**Submitting a Shot**

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/PSubmitter.JPG

Queue a single shot by activating it and choosing 'Submit Shot'. Submit mutliple shots by enabling them in the shot list and choose 'Batch Submit Shots'. Job name and project name are required. Jobs names will be replaced with shot name when batch submitting. Pandora will save local copies of the project and queue jobs in Pandora Handler. Using this submitter will force **absolute** file paths, ensure remote nodes have network access to all required paths.

**Multi-Layer EXR**

Pandora does not officially support multi-layered EXR renders and output nodes using this format. This is to streamline the application for the Prism Pipeline, Shot Manager however offers in-built support for automatically outputing passes with some filtering options using the Shot List node. 

To render Multi-Layered EXRs you'll need to replace a python file in on **each render node** to bypass Pandora's limitation; 
find --Install directory--"\Pandora\Plugins\Apps\Blender\Scripts\Pandora_Blender_externalAccess_Functions.py". Make a Backup of this file.
Replace with ShotManager.zip(extract)"\Shot Manager addon\shot_manager_pro\Pro\Pandora_Blender_externalAccess_Functions.py" .Remember to submit with a **new project** name not previously used, or manually delete older jobs.

**Trouble Shooting**. Pandora Core has an issue where it will often lose track of components; Coordinator.exe and Slave.exe. Therefore, the status shown in the panel might not match the actual states of these processes. This occurs especially when a process has been closed or crashed, outside of control from its settings component. Use 'Reset Pandora' to clear Coordinator and Slave states on the local machine. Make sure to close those processes(.exe) if already running, otherwise you might launch duplicate processes.

B-Renderon! Integration
=======================
Launch B-Renderon with shots loaded as seperate blend files. Requires B-renderon v2 or above. The executable path for B-renderon must first be entered in Blender Preferences -> add-ons -> Shot Manager settings   

Compositor Nodes
----------------

Shot List Node
==============
**IMPORTANT!** for compositor nodes to have any effect, compositor 'Use Nodes' must be enabled. Node groups containing Shot Manager nodes are currently unsupported.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/ShotlistNode.JPG

The Shot List node is central to the Shot Manager nodes and is required for Constructor nodes and Multi-Switches. **A maximum of one shot list node should exist.**

**Path:** The displayed path is the projects output directory. The target folder and filenames are automatically named after the active shot. File paths are converted to absolute paths. If the Constructor nodes aren't connected to the Path Format socket, the path consists of; Root directory + shot name(folder)+ shot name + '_'(filename). However the scene render path in Blender's output settings will vary when 'Separate Layers' is active. 

**Multi-Switch** will create a new node group dynamically linked to active shots.
**Primary-Switch** will create a new Render Layer node which automatically switches the input View Layer to the active Shot's Primary Layer, else mute.
**Refresh**, non-essential node update. Although shot Manager nodes are updated upon shot change, setting or property changes, changes outside of Shot Manager won't be reflected immediately. For example adding new light passes to a View Layer. Shot Manager will update before any rendering. 

**Sync Output Paths**. Only Available if Separate Layers is disabled. Output nodes created by the user are updated so their base path matches the output path set by the Shot List node and the active shot.

**Shot List and saved states**. Here you can select and queue shots for bath export. Each shot displays the saved states for View Layers. These states can be toggled (renderable/non-renderable), removed or added. 

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/remap.JPG


**Path Format**. String input socket for path 'Constuctor' nodes.

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/ShotlistNode2.JPG

**Separate View Layers**
Automatically generate noes to output view layers for external compositing. NOTE: nodes are generated upon any update made within the add-on, therefore generated nodes should not be directly edited. Output files will be named according to the layer name.  **You May want to delete the Composite node** when seperating layers.

**Separate Passes**
Optionally separate view layer light passes.
**Shot Name in Prefix (non-EXR MultiLayer)**
if using Seperarate View Layers, the option to add the shot names into the output file pre-fix is available.

**Preview** Make the output group an 8bit png for preview renders.

**Exclude/Include** passes from being output, not case sensitive. Pass names should be seperated by commas.

**EXR MultiLayer output**

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/EXR_layers.JPG 

When using "Separate Passes", Output Groups add and define output file names. Filter Render Passes using exclusion keywords separated by commas, no spaces, not case-senisitve. Including filename options 'Shot Name' and 'View Layer' name will be added to the given filename.  

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
* Output Node, uses the custom name of the output node, useful for exporting EXR's without overiding the default output/composite (which will use the custom 'main output text'), or to avoid duplicate filenames when using multiple output nodes.


Collections Inspector Node
==========================
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Collections.JPG

An alternative interface for overseeing and modifying collection states per View Layer. This aims to bring back the kind of oversight possible in Blender 2.7 where layer visibility, holdout and indirect states were layed out in view layer settings. It can also be used to keep track of very complex scenes with many nested collections. Setting the View Layer to 'Active View' will use the currently active view layer. Changing the view layer in the drop down menu will not change your currently active view layer. This can be quicker in large scenes to avoid loading objects.

Output Viewer Node
==================
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Output_Viewer.JPG
Use to count matching output files in all output paths. If a folder or file is detected you may click the folder icon to open the directory in your OS explorer or click the image icon to load it in an open Blender Image Editor. Files are counted after rendering or when the refresh button is clicked.

Multi-Switch
============
.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/MultiSwitch.JPG
The Multi-Switch is a handy node group that generates inputs per shot. The active input is connected internally depending on the active shot. This allows the user to have multiple node graphs pointing to the Composite Node and only render the relevant one to the active shot. **Do not modify this node's name, group name or internal nodes. Requires a Shotlist Node** 


Known Issues
------------
**Pandora Submitter**. 'Cannot read json file' error may occur, has no impact on the render.

**Missing file explorer options** . This can occur when going between versions of Blender. SOLUTION- Restart Blender , disable 'Load UI' first when opening. 

.. image:: https://raw.githubusercontent.com/OtherRealms/Shot-Manager-/master/Load%20ui.JPG 



