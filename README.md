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

- Both Alexandra and Bella discussed security issues of the product. 

## Cardboard Prototyping

We decided that we needed to design the pill release mechanism first, before we considered involving facial recognition and user interaction. We built a cardboard prototype to test this behaviour.

###  Design 1

After considering all design methods discussed above we selected the 2nd prototype design to observe further. We created a cardboard prototype that uses a turstile mechanism to deliver the pills. the prototype is demonstrated in the video below.

https://youtu.be/GEepd2mpEjM

##### Releasing pills

As mentioned above we implemented a turnstile mechanism with cardboard and the servos to release pills. The video below shows how the prototype uses this mechanis to release the pills when the button is pressed.

https://youtu.be/7yktiRSzXLk

##### Results

The turnstile performed well in delivering the pills but the prototype had severe limitations. It. can only hold one pill in each tunel at a time. This was our next design challenge.
