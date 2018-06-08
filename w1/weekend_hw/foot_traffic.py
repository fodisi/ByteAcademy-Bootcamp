#Foot Traffic Analysis
#=====================

#A very prestigious art gallery has contacted you regarding a job. Get to work! 

#Management wants to figure out how many people visit each room in the gallery, and for how long: this is to help improve the quality of the overall gallery in the future.

#Your goal is to write a program that takes a formatted text file that describes the overall gallery's foot-traffic on a minute-to-minute basis. From this data you must compute the average time spent in each room, and how many visitors there were in each room.

####The Input

#Each line in the text file represents either a visitor entering or leaving a room. It starts with an integer, representing a visitor's unique identifier. Next on this line is another integer, representing the room's number. Next is a single character, either 'I' (for "In") for this visitor entering the room, or 'O' (for "out") for the visitor leaving the room. Finally, at the end of this line, there is a time-stamp integer: it is an integer representing the minute the event occurred during the day. All of these elements are space-delimited.

#You may assume that all input is logically well-formed: for each person entering a room, he or she will always leave it at some point in the future. A visitor will only be in one room at a time.

#Note that the order of events in the log are not sorted in any way; it shouldn't matter, as you can solve this problem without sorting given data.

#Sample Input:

#        0 0 I 540
#        1 0 I 540
#        0 0 O 560
#        1 0 O 560

####The Output

#For each room that had log data associated with it, print the room number, then print the average length of time visitors have stayed as an integer, and then finally print the total number of visitors in the room. All of this should be on the same line and be space delimited; you may optionally include labels on this text, like in our sample output 1.

#Sample Output:

#        Room 0, 20 minute average visit, 2 visitor(s) total

####Loading the Text File

#You'll find a text file `traffic.txt` in this repo. Import this text file and parse it to get the results.

#When you are done solving the problem, write your output to another text file and save it in the repo.


#!/usr/bin/env python3

from enum import Enum


#represents the possible status of a visit
class VisitStatus(Enum):
    OPEN = 1,
    CLOSED = 2


#represents a visit that a visitor does to a art gallery's rooms
class Visit():
    def __init__(self, visitor_id):
        self.__visitor_id = visitor_id
        self.__start_time = -1
        self.__end_time = -1
        self.__status = VisitStatus.OPEN

    #starts a visit. takes the entrance time as parameter (int)
    def start(self, time):
        self.__start_time = time

    #finishes a visit. takes the exit time as parameter (int)
    def finish(self, time):
        self.__end_time = time
        self.__status = VisitStatus.CLOSED

    #returns the staus of a visit.
    #It will be one of the possible values of enum VisitStatus.
    def status(self):
        return self.__status

    #returns the duration of a visit
    def duration(self):
        return self.__end_time - self.__start_time

    #print the visit
    def print(self):
        print('id {0}, start {1}, end {2}, status {3}'.format(
            self.__visitor_id,
            self.__start_time,
            self.__end_time,
            self.__status))


# represents a visitor of a art gallery's rooms
class Visitor():
    def __init__(self, id):
        self.id = id
        self.__visits = []

    #starts a visit for an instance of visitor. takes the entrance time as parameter (int)
    def start_visit(self, time):
        if self.has_open_visit():
            raise Exception('Visitor {0} already has an open visit.'.format(self.id))

        new_visit = Visit(self.id)
        new_visit.start(time)
        self.__visits.append(new_visit)

    #finishes a visit for an instance of visitor. takes the exit time as parameter (int)
    def finish_visit(self, time):
        if not self.has_open_visit():
            raise Exception('Visitor {0} has no open visit.'.format(self.id))

        self.get_open_visit().finish(time)

    #returns true if the visitor has open visits. otherwise, returns false
    def has_open_visit(self):
        return self.get_open_visit() != None

    #returns the open visit for the instance of visitor. otherwise, returns None
    def get_open_visit(self):
        for v in self.__visits:
            if v.status() == VisitStatus.OPEN:
                return v
        return None

    #returns the number of visits done by the instance of visitor
    def count_visits(self):
        return len(self.__visits)

    #returns the average duration of all visits done by the instance of visitor
    def average_visit_duration(self):
        total_time = 0
        for visit in self.__visits:
            total_time += visit.duration()

        return total_time / self.count_visits()

    #prints all the visits done by the instance of visitor
    def print_visits(self):
        print("All visits for visitor '{0}'".format(self.id))
        for v in self.__visits:
            v.print()


#represents a Art Gallery's room
class Room():
    def __init__(self, id):
        self.visitors = {}
        self.id = id

    #records that a specific visitor has entered the room.
    #takes the visitor id (int) and entrance time (int) as parameters
    def visitor_enters(self, visitor_id, time):
        if not visitor_id in self.visitors:
            new_visitor = Visitor(visitor_id)
            self.visitors[visitor_id] = new_visitor

        self.visitors[visitor_id].start_visit(time)

    #records that a specific visitor has left the room.
    #takes the visitor id (int) and exit time (int) as parameters
    #raises an Exception if visitor_id is not in the current list of visitors.
    def visitor_leaves(self, visitor_id, time):
        if not visitor_id in self.visitors:
            raise Exception('Visitor {0} has not entered this room {1}".'.format(visitor_id, self.id))
        self.visitors[visitor_id].finish_visit(time)

    #returns the number of visits to the room.
    # if the same visitor enters the room twice, the visit is counted twice.
    def count_visits(self):
        count = 0
        for item in self.visitors.items():
            visitor = item[1]
            count += visitor.count_visits()
        return count

    #returns the number of visitors to the room.
    # if the same visitor enters the room twice, the visitor is counted just once.
    def count_visitors(self):
        return len(self.visitors)

    #returns the average duration of all visits done by the instance of visitor
    def average_visit_duration(self):
        total_time = 0
        for item in self.visitors.items():
            visitor = item[1]
            total_time += visitor.average_visit_duration()
        return total_time

    #prints a summary of the room's visits
    def print_visit_summary(self):
        message = 'Room {0!s:0>3}, {1!s:0>5} minute(s) average visit, {2!s:0>3} visits(s) total, {3!s:0>3} visitors'
        print(message.format(self.id, self.average_visit_duration(), self.count_visits(), self.count_visitors()))


#represents an Art Gallery
class Gallery():
    def __init__(self):
        self.rooms = {}

    #adds a new room to the art gallery's room list
    def __add_room(self, room_id):
        room = Room(room_id)
        self.rooms[room.id] = room

    #updates the traffic (entrances and exits) in the art gallery's rooms.
    #takes the visitor_id(int), room_id(int), flow_type(string = "I" or "O"), and time(int) as parameters.
    # raises an Exception if "flow_type" is not valid ("I" or "O")
    def __update_traffic(self, visitor_id, room_id, flow_type, time):
        #raises exception if flow type is invalid.
        if flow_type not in ["I", "O"]:
            raise Exception('Invalid flow type. Expecting "I" or "O". Received "{0}".'.format(flow_type))

        #if room does not exists, creates a new one. otherwise, assigns the existing one.
        if not room_id in self.rooms:
            self.__add_room(room_id)
        room = self.rooms[room_id]

        #register if the visitor is entering or leaving the room.
        if flow_type == "I":
            room.visitor_enters(visitor_id, time)
        else:
            room.visitor_leaves(visitor_id, time)
            
    #loads foot traffic data from a .txt file
    #every line represents a traffic event (entrance or exit).
    #each line must contain 04 data elements, separated by single space
    #line[0]: visitor_id; line[1]: room_id; line[2]: flow("I"/"O"); line[3]: time
    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                str_values = line.rstrip('\n').split()
                if len(str_values) > 0:
                    self.__update_traffic(
                        int(str_values[0]), #visitor_id
                        int(str_values[1]), #room_id
                        str_values[2], #flow_type: I/O
                        int(str_values[3]) #entry_time
                    )

    #prints art gallery's visit history
    def print_visit_history(self):
        for item in self.rooms.items():
            room = item[1]
            room.print_visit_summary()


if __name__ == '__main__':
    g = Gallery()
    g.load_from_file("traffic.txt")
    g.print_visit_history()

