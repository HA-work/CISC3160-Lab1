// Name: Hassan Akbar
// Class: CISC 3160 
// Section: MY11
// Professor Chuang
// Assignment 1

//*********************************************************************************

 class Artist {
  
    public String name; // artist name
    public int timesAppeared; 
    public int artistViews;
    
    // could change these to private
    // then need setters and getters
    
//*********************************************************************************    
    
 //No-Arg Constructor
 
 /* Method public Artist():
  * 
  * Input:
  *    None
  * Process:
  *    creates Artist object
  *    Sets Strings data members to null string
  *    sets int values to 0
  * Output:
  *    None
  */
    
    public Artist() {
  
     name = "";
     timesAppeared = 0;
     artistViews = 0;

   }
    
    
 //*********************************************************************************    
//Parametized Constructor
 
 /* Method public Artist(String n, String num, String views):
  * 
  * Input:
  *    String n the artists name
  *    int num the times the artist appeared
  *    int v the views of the artist
  * Process:
  *    creates Artist object
  *    Sets the parameters to the input
  *   
  * Output:
  *    None
  */
   
    public Artist(String n, int num, int views){
      
      name = n; // set artist name
     
      timesAppeared = num;
      artistViews = views;
     
     
    }
    
    
//*********************************************************************************    
    
    
 /* Method String toString():
  * 
  * Input:
  *    None
  * Process:
  *    makes a formatted string
  * Output:
  *    Returns a formated string of the Artist object for printing
  */
 //toString() method - uses String static method .format()
 public String toString() {
  String str = String.format("%-25s %-25d %-25d", name, timesAppeared,artistViews);
  
  return str;
 }

    
//*********************************************************************************   
    
}