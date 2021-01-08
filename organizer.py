from tkinter import *
from tkcalendar import *
from tkinter import messagebox as mb

root = Tk()
root.title('Event Organizer')
# root.geometry("600x400")

canvas1 = Canvas(root, width = 400, height = 400)
canvas2 = Canvas(root, width = 400, height = 400)

dataFile = "OrganizerEventData.txt"

headerInfo = Label(root, text = "Select any date and click the button below to get started!")

cal = Calendar(root, font = "Calibri", background = "brown", selectmode="day", headersbackground = "light gray", bordercolor = "black", showweeknumbers = False, borderwidth = 5, weekendbackground = "white", othermonthbackground = "grey", othermonthforeground = "grey", othermonthweforeground = "grey", othermonthwebackground = "grey", weekendforeground = "black")

canvas1.create_window(200, 40, window = headerInfo)
canvas1.create_window(200, 180, window=cal)



# cal.geometry("600x400")
# cal.pack(pady=200)
# cal.pack(padx=200)





def dateSelect():
   selectedDate = cal.get_date()
   selectButton.pack_forget()
   dayStartPos = selectedDate.find("/")
   selectedMonth = selectedDate[0:dayStartPos]
   if (len(selectedMonth) < 2):
      selectedMonth = '0' + selectedMonth
   
   selectedDate = selectedDate[dayStartPos + 1:]
   yearStartPos = selectedDate.find("/")
   selectedDay = selectedDate[0:yearStartPos]
   
   
   if (len(selectedDay) < 2):
      selectedDay = '0' + selectedDay   
      

   selectedYear = "20" + selectedDate[len(selectedDate)-2:]

   selectedDateFormatted = selectedDay + "/" + selectedMonth + "/" + selectedYear
   
   # msg = mb.askokcancel("Test", selectedDateFormatted)
   
   

   description = Label(root, text = "Event for " + selectedDateFormatted + ": ")
   inputBox = Entry(root)
   
   def addTask():
      f = open(dataFile, "a")
      eventDetails = inputBox.get()
      if(len(eventDetails) == 0):
         mb.showwarning(message = "Empty Event Description!")
      else:
         f.writelines(selectedDateFormatted + " " + eventDetails + "\n")
         f.close()
         mb.showinfo(title="Event successfully added!", message = "Event: " + '"' + eventDetails + '"' + " successfully added for " + selectedDateFormatted)
         
         
   def removeTask():
      f = open(dataFile, "r")
      lines = f.readlines()
      
      userInput = inputBox.get()
      
      try:
         taskToDelete = int(userInput)
         counter = 1
         with open(dataFile, "w") as f:
            for line in lines:
               if(line[:10] == selectedDateFormatted):
                  if(counter != int(taskToDelete)):
                     f.write(line)
                  counter += 1
         if(counter <= taskToDelete):
            mb.showwarning(title = "Value error!", message = "Event number could not be detected in events for " + selectedDateFormatted)
      except ValueError:
         mb.showwarning(title = "Invalid Input!", message = "Please enter a valid event number for deletion!")
   
   
   
   
   inputButton = Button(root, text = "Add event", command = addTask)
   doneButton = Button(root, text = "Return to Calendar", command=returnButton)
   deleteButton = Button(root, text = "Delete event", command = removeTask)
   
   def displayEvents():
      canvas3 = Canvas(root, width = 400, height = 400)
      file1 = open(dataFile, "r")
      Lines = file1.readlines()
   
      counter = 1
      textToDisplay = ""
      for line in Lines:
         if(line[:10] == selectedDateFormatted):
            textToDisplay += str(counter)
            textToDisplay += ". "
            textToDisplay += line[10:]
            textToDisplay += "\n"
            counter += 1
                  
      
      headerText = "Showing events for " + selectedDateFormatted + ": "
      if(textToDisplay == ""):
         headerText = "There are no listed events for " + selectedDateFormatted
         
      
      
      def returnButton2():
         textToDisplay = ""
         displayedEvents = Label(root, text = textToDisplay)
         canvas3.destroy()
         canvas2.pack()
      
      headerDisplay = Label(root, text = headerText)
      returncavas2 = Button(root, text = "Exit", command = returnButton2)
      displayedEvents = Label(root, text = textToDisplay)
      
      canvas3.create_window(200, 30, window = headerDisplay)
      canvas3.create_window(30, 30, window=returncavas2)
      canvas3.create_window(200, 200, window=displayedEvents)
      
      canvas3.pack()
      canvas2.pack_forget()
      
      
   showButton = Button(root, text = "Show events for this day", command=displayEvents)
 
 
   canvas2.create_window(120, 100, window=description)   
   canvas2.create_window(250, 100, window=inputBox)
   canvas2.create_window(175, 150, window=inputButton)
   canvas2.create_window(181, 200, window=deleteButton)
   canvas2.create_window(210, 250, window=showButton)
   canvas2.create_window(196, 300, window = doneButton)

   
   canvas1.pack_forget()
   canvas2.pack()
   

   
   # msg = mb.askokcancel("Test message", selectedDate)
   # msg.pack()
        



def returnButton():
   canvas2.pack_forget()
   canvas1.pack()
   
   


selectButton = Button(root, text = "Select Date", command = dateSelect)
canvas1.create_window(200, 330, window=selectButton)
canvas1.pack()
   
   
root.mainloop()
