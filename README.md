# Interactive Device Design Final Project
Donal Lowsley-Williams (dml333)
Kristjan Ari Tomasson (kt479)
Alex Legarda Jagoras (al926)

## The Automated Pill Dispenser 
The main idea is to create an automated pill dispenser that selects the correct pills and correct quantities based on the day of the week. When someone approaches the pill dispenser, it will detect their face and greet them. Then, based on the day of the week and the individual involved, it will retrieve the respective pills. This will help solve the problem of polypharmacy many users face that are under a variety of medication.

**Storyboard**

 <img width="622" alt="Screen Shot 2021-11-18 at 10 03 35 AM" src="https://user-images.githubusercontent.com/52221419/142440765-d76006d7-2d3b-45fb-95ab-c82bff230cdb.png">
 
 **Verplank Diagram**
 
 <img width="687" alt="image" src="https://user-images.githubusercontent.com/42963791/142444470-8ad23ffa-b95d-400b-9054-e3c9cdff414e.png">
 
### Risks & Contingencies
- Dispensing too many or the wrong pills
- Dispenser getting stuck (should have a failsafe or easy way to manually get the pills out)
- Duplicate dispensing - the dispenser should only dispense pills once per day (or as
many times as necessary, but never more)
- Dispenser doesn't detect the correct face and releases pills that belong to another
individual


### What We'll Need
- Raspberry Pi
- Servo controllers
- Camera
- Speaker
- 3D printed turnstile 
- 3D printed “slide” 
- LCD Screen
- Cardboard

### Prototype Designs
<img width="769" alt="Screen Shot 2021-11-18 at 10 54 53 AM" src="https://user-images.githubusercontent.com/52221419/142449922-8a8b0da3-6caa-4a21-8521-e7057e7b264a.png">

## User feedback

Below are the commets we received on canvas:

##### Sara Wang

This is a great idea. Since some medications are taken not on a daily basis, but rather multiple times a day, an extension could be to add a way to customize the daily schedule. You could also consider pairing the device with a notification system/tracker that reminds the user to take their medication at the times/days they need to and logs when they have done it.

##### Alexandra Walburgis Dongfangchen Bremers

It is a nice idea and well documented. I like that you thought about the context of use and the user, but also about how the system will be packaged. I wonder what you wanted to 3D print? From the description of the device it seems more suitable to use cardboard prototyping or existing packaging materials (e.g. don't print a box!). Additional considerations that could make the project stronger could be the inclusion of a security feature, or considerations around the fact that eyesight characteristics might make it hard for the user to read from a small display.

##### Bella Baidak

Very useful idea!! I often forget to take my daily pill/vitamins and having a device like this would surely help me a lot. 
A concern I have for this project are the risks you pointed out. If someone gets the wrong amount of pills or the face detection messes up and gives the pills to the wrong person. This are very severe risks and can lead to horrible side affects. It would be beneficial to incorporate some risk prevention into our design or some protocols. What are some ways you can think of that could prevent these risks? Two ideas off the bat I have are: having a weight sensor that detects the weight of pills dispensed and if the wrong weight (too many pills are dispensed) then the user is informed.  Another idea is that if the CV model is lets say less than 95 percent (some threshold you choose) sure that they have detected them correct face, then have the user type in a password (there is a key pad piece that would work nicely for this). 
Overall I think your group will be able to execute your project as planned, it seems very doable to me and I am excited to see it! I did a sort of similar project for one of my labs and I used the servo motor with cardboard attached to dispense the pills, feel free to check it out on my github for inspiration. I cant paste a link here but my github user name is sketh444 and its under the interactive-lab-hub, under lab 5

### Feedback summary

We were very grateful for the feedback we received, it was thorough and detailed. The main higlights and action points are listed below.

- Sara pointed out an interesting way to improve out product by allowing users to cutomize their schedule. We really like this idea nd plan to desing a method to interact with the settings of the device; how may pills to release of what kind, who owns which pills, how often to release them a day, etc. We plan to implement a simple gui to take care of this that will be remotely connected to the device.

- Sara also suggested we included some notification system for the users. This would be a very nice feature for our product and make sure users do not have to go into their bathroom to remember to take their pills. We plan to include this feature by using sound and light otifications and if all goes well it would be useful to be able to sed otifications to user's personal devices; e.g. smart phones.

- We will follow Alexandra's suggestion and not do any 3D printing unless we have properly tested it with cardboard first.

- Both Alexandra and Bella discussed security issues of the product. We had listed this as a risk earlier as well and it was helpful to get a confirmation from users that this was a big concern. We acknowledge that the face-recognitionn can someties produce errors ad hence we like the idea of some confirmation feature. We are planning to implement a voice confirmation feature so that the device doesn't release ay pills unless the user confirms it is him via voice input. We also like the weight scale idea to make sure that the correct pills were released. When reading the feedback we also had the idea of solving that problem in a similar manner as we did in Lab 5 where we use object detection to check if the right amount of pills were released.

Overall, we appreciate the feedback we got and have creatred the following action items for our product:

- Include a GUI to interact with the settings of the device

- Implement a notification system

- Have users confirm their identidy before pills are released

- Include a confirmation check to make sure the device released the correct amount of pills

## Cardboard Prototyping

We decided that we needed to design the pill release mechanism first, before we considered involving facial recognition and user interaction. We built a cardboard prototype to test this behaviour. A simple button is used to control the pill dispenser.

###  Design 1 - Turnstile

<img width="548" alt="image" src="https://user-images.githubusercontent.com/42963791/145081162-ac70446e-851a-471e-b630-e3598986d483.png">

<img width="552" alt="image" src="https://user-images.githubusercontent.com/42963791/145081560-8a7764e1-8dd7-40b9-9ef2-1fc6730d461a.png">

After considering all design methods discussed above we selected the 2nd prototype design to observe further. We created a cardboard prototype that uses a turstile mechanism to deliver the pills. The prototype is demonstrated in the video below.

https://youtu.be/GEepd2mpEjM

##### Releasing pills

As mentioned above we implemented a turnstile mechanism with cardboard and the servos to release pills. The video below shows how the prototype uses this mechanis to release the pills when the button is pressed.

https://youtu.be/7yktiRSzXLk

###### The turnstile

<img width="403" alt="image" src="https://user-images.githubusercontent.com/42963791/145081448-0f34b8e6-0287-4ca3-88df-5997cd00cc36.png">


### Results

The turnstile performed well in delivering the pills but the prototype had severe limitations. It can only hold one pill in each tunel at a time, if more pills are put in the pipes, there is no mechanism to control how many are released. Someties a few go through and other times they get stuck and no pills go through. This was our next design challenge.

### Desig 2 - Gear system

To try to solve the problem of releasing one pill at a time we took a look at other design choices. We looked at designs of excisting pill dispensers, gun magazines, pet food feeders, etc. Those are all devices that allot a given amount of pills/bullets at a time. We observed that most of those devices have a compartment that has space for a given amount of pills and this compartment is then emptied to release pills before being automatically filled again.

We designed a funnel out of cardboard that only allows one pill through it's narrowest part at a time, the funnel is connected to a tunnel that has space for one pill. In the tunnel there is a piece that is connected to a rack. The servo then spins the gear to move the piece back and forth, pushing the pill out and creating space for the next pill. The prototype was made with LEGO pieces and cardboard in the Maker Lab.

<img width="550" alt="image" src="https://user-images.githubusercontent.com/42963791/145266548-fd9bf10c-4a84-457e-8941-3956fe22f721.png">

<img width="552" alt="image" src="https://user-images.githubusercontent.com/42963791/145266588-6dd9e76b-ebdf-438a-a844-29e85ca20857.png">

<img width="520" alt="image" src="https://user-images.githubusercontent.com/42963791/145266626-51eb8c32-ba70-44ee-922d-1a105e16763b.png">

The gear rack

<img width="548" alt="image" src="https://user-images.githubusercontent.com/42963791/145269560-ff2aae62-654b-4c74-89fe-876b7e4dcbf8.png">

The prototype is explained in the video below.

https://youtu.be/psr20-aDSgY

### Results

The prototype was successful in delivering one pill at a time. You can pour pills into the funnel and the device delivers one pill at a time. The main issues were related to the gear rack/saw and mounting units properly. The gear rack was made of cardboard (see above) and the device needed a little help to be held together. However, the prototype showed that this design can be successful in delivering the pills. The next step was to craft it more carefully and re-structure it to make the device more robust. We aim to 3d prinnt the gears to make sure the device not fall apart when used as the cardboard tended to do.

## 3D Printinng

Having observed different designs with cardboard prototyping it was time to make a more robust prototype with 3D printing. We used the best design we had observecd so far and found a 3D model of a very similar design [online](https://www.thingiverse.com/thing:4673805). The design is based on a gear controlled by the servo which controlls the release of pills by movig a saw rack to fetch one pill at a time exactly like cradboard prototype 2 above.

The device is made from 4 componets which are displayed below.

###### Saw rack

<img width="974" alt="image" src="https://user-images.githubusercontent.com/42963791/145484402-f3036b72-5896-49da-9827-9208011fe63d.png">

###### Gear

<img width="976" alt="image" src="https://user-images.githubusercontent.com/42963791/145484429-c51d60be-79ba-42ca-b36a-3b01f61c426b.png">

##### Tunnel

<img width="975" alt="image" src="https://user-images.githubusercontent.com/42963791/145484452-5f43c009-cce9-4d41-9a76-b653b7501b0b.png">

##### Pill holder

<img width="971" alt="image" src="https://user-images.githubusercontent.com/42963791/145731008-6564acdb-d41b-44ee-abbd-b1015b33b5bd.png">

The pill releasig mechanism is demostrated below.

https://youtu.be/-unlCLesPGM

### Results

As can be seen in the video, the 3D printed releasing mechanism was successful in delivering multiple pills. Having developed the mechanism for releasing pills we had to design the device itself and how users would interact with it. These steps are discussed below. (In the video above we have already created the box ind interaction that are described below.)

## Involvig other components

Having designed the pill releasig system the next step was to include user iteraction. The device will be controlled through a remote GUI that allows the user to selcet which pills he takes and on which days. The device will also be activated by face detection and the cotrolled through voice commands and gestures. The original plan was to use face recognition but aftersome experimentation and research online we realised the hardware we have was not capable of fully handling that task. It is possible to do some facial recognition with a raspberry pi but the accuaracy is not good and it does not handle changing backrounds for example, as it uses image recognition in most cases. We did some experiments from [these](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/) instructions but the recognition was not accuarate enough. A pill dispenser is a critical device (as explained in the comments above) and can not make errors, hence we do not want to risk errors by involving flaky facial recognition. However, we are happy with the new plan and feel that face detection followed by voice commands is a user friendly and safe method. 

#### Device Control and GUI

We implemented a graphical user interface usin tkinter where users can enter how many pills of each sort they need to take each day. The device then uses this information to detirmine how many pills of each kind to release each day. The GUI is demonstrated in the video below.

#### Face detection and voice control

The device is contantly looking to detect faces. Once it detects a face it promts the user to say his name and then the device outputs the correct pills for that user for the given day. This is demonstrated in the videos below. In the first one the user says a name that is o file and gets his pills. In the second one, the user says a name that is not on file and does not get any pills.

Name on file

https://youtu.be/wwhEHTIEWZ4

Name not on file

https://youtu.be/8cJcsOLmWMg

## Designing the device

##### Contructiong the body of the device

We used cardboard as the main component to construct the device. After measuring the size of all the internal components we created a box of suitable size that would fit them all. This process is displayed in the images below.

<img width="551" alt="image" src="https://user-images.githubusercontent.com/42963791/145731926-94b825bb-d86d-4cee-9879-ea1e5a352d21.png">

<img width="552" alt="image" src="https://user-images.githubusercontent.com/42963791/145731934-5593653c-e6e7-4e4a-b210-693a0557a650.png">

The next step was to place all the components inside the device. We started with the camera. The camera we have is a little bulky and we wanted to hide it from the end user. We placed it inside the box and cut a hole in it so the lens was only visible from the outside.

<img width="543" alt="image" src="https://user-images.githubusercontent.com/42963791/145732059-ba9718f4-8a67-42a2-84ef-1ab3be71369d.png">

<img width="538" alt="image" src="https://user-images.githubusercontent.com/42963791/145732064-8325776e-b4e2-4f85-b0de-59dddd89c39b.png">

Next, we had to fit the pill dispensing uits into the device. We had to ensure that the servo and the gear system were properly mounted to make sure they would function properly. We mounted the servo to the bottom of the box and cut precisely measured where to cut holes in the bow for the pill dispensing unit to align them with the servo. Each dispensing unit required two holes, one to insert pills and oe to release pills. The servo then spins the gear which moves the saw rack back and forth. This design is displayed below.

<img width="732" alt="image" src="https://user-images.githubusercontent.com/42963791/145732302-8a00a01e-989f-49db-8f6c-c88d0e8c8d68.png">

<img width="972" alt="image" src="https://user-images.githubusercontent.com/42963791/145732288-cbf39553-2265-4e95-a301-9eadc727d000.png">

<img width="714" alt="image" src="https://user-images.githubusercontent.com/42963791/145732315-b90f6cb1-79a3-474a-8cfb-81b955da3d02.png">

The final step was to place the PI in the box and close it off. We decided that we wanted the PI to be accessible so we did not want to close the device completely. Another design challege was that the microphone had to be on the outside of the box for the voice control to work properly. This was solved by having a lid on the backside of the device that could be opened to access the device. The microphone was then put in a small sidebox that was open in the frot to allow it to detect sound from thew outside. 

The back can be opened to access PI

<img width="965" alt="image" src="https://user-images.githubusercontent.com/42963791/145732527-cddc49c2-03c7-4c0b-b420-113517f7bf43.png">

<img width="966" alt="image" src="https://user-images.githubusercontent.com/42963791/145732539-001e0dd6-e482-42b9-96f0-8d96ad9acacd.png">

There is an opening on the right side to allow the microphone to detect voice input

<img width="969" alt="image" src="https://user-images.githubusercontent.com/42963791/145732558-91890cac-d13e-4478-a29a-64791da1ffa3.png">


