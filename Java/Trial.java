// Name: Hassan Akbar
// Class: CISC 3160
// Section: MY11
// Professor Chuang
// Assignment 1

//*********************************************************************************

import java.io.*; // import file class
import java.util.Scanner; // import scanner
import java.util.ArrayList; // import array list

public class Trial {
  
//*********************************************************************************
 public static void main(String[] args) throws IOException {
   

  
   // quicksort would also be a better sorting method to use
   // could create my own quicksort
   // the built in quicksort would probably not work
   // because case sensitivity
   // I want the Output to go A, a B, b... Z, z
   // instead of A-Z, a-z

   
   
   
   ArrayList<Artist> arrayOfArtists = new ArrayList<Artist>(); 
   
   // could also make a song list
 
  

     
//*********************************************************************************     
     
   // open and read the input file
   // could be made a method
  
  
   
   // error file
   // will have any errors
   
   PrintWriter errorFile = new PrintWriter("errors.txt");   // file
    
   errorFile.println(" Hassan Akbar"); 
   errorFile.println(" CISC 3160");
   errorFile.println(" Professor Chuang");
   errorFile.println(" HW 1");
   errorFile.println();
     
   // maybe add a way to check if the errors in the file have been corrected  
   // someone would need to manually remove the extra commas
   
   // could store these intsead of printing directly as it is bad practice
   
   errorFile.println("List of errors and line they appear on" );
     
   errorFile.println();
   
   // Inputfile
   File inFile = new File("input.txt");
     
   

   //create Scanner object
   Scanner sc = new Scanner(inFile, "UTF-8");
   
       
   String line;
     
   line = sc.nextLine();// skip unneeded line
   line = sc.nextLine(); // skip unneeded line
   // 3rd line is where the data starts
     

   int totalViews = 0;
   int problemEntries = 0;
   int lineCount = 3; // 3 as we skipped the first two lines
   int songCount = 0; // number of songs read in
   
     
   while (sc.hasNext() ) {
  
      
     //read next line of data 
     line = sc.nextLine();
       
     // data stored as
     // position,    track name,    artist,     streams,      url
   
     String[] tokens = line.split(","); //tokenize a String using method split()
     // problem with splitting when song names have , in the title
     // can't think of a way to account for it
     // could count the number of tokens and if it is greater than index 4
     // this means a problem happened
     // dont know how to tell where the problem happened and correct for it though
     // can use the array.length data member to see how many tokens are made
     // if length is gretater > that 5 there is a problem
     // could skip this entry
     // not sure how to fix it without actually seeing where the problem is
     // errors are placed into a file
     
     // an arraylist of setings for errors
     
     
     
     // search for the error
     
     
     
     if (tokens.length == 5){ // proper case
        
       
       String artistName = tokens[2];
   
       artistName = artistName.replaceAll("\"" , "");
       //remove the "" around some names
   
       String views = tokens[3];
   
       int v = Integer.parseInt(views);
   
       totalViews = totalViews + v;
   
       boolean newArtist = true;
   
    
     
     
     
     
       for(int i=0; i < arrayOfArtists.size(); i++){
       
         // checking if the artist name is repeated
         // could be done seperately but probably better to search while making 
         // the array 
         // if repeated we increase the times appeared and add to the views
            
       
         Artist checkArtist = arrayOfArtists.get(i);
         if(checkArtist.name.equals(artistName)){
         
           checkArtist.timesAppeared++; // could type out full +1
           checkArtist.artistViews = checkArtist.artistViews + v; // could use += shorthand
           newArtist = false;
         
         }
       
       
       
       }
     
     
     
     
   
       if (newArtist == true){
     
         Artist tempArtist = new Artist(artistName, 1, v);
         arrayOfArtists.add(tempArtist);
     
   
     
       }
   
       lineCount++;
       songCount++; // song count up
        
        
        
     } else {
        
        
           
        problemEntries++;
        
        errorFile.println("Error Number: " + problemEntries  );
        errorFile.println("Error on Line Number : " + lineCount);
        
        // add number of errors to the start?
        // would need to save the errors and print them later
        
        errorFile.println(line);
        errorFile.println();
       
        
        
     }
      
      
     
     
     
   
   
 
   }
     
     
   sc.close();
   
   
   
   errorFile.println();
   errorFile.println("Number of Errors: " + problemEntries);
   
   
   errorFile.flush();
   errorFile.close();
   
   
//*********************************************************************************        
   // print initial array
   // the array is unsorted
   // could make this a method
     
     
     
   PrintWriter outFile1 = new PrintWriter("myoutput1.txt");   // file
   // PrintWriter outFile = new PrintWriter(System.out); // screen
     
    
     
   outFile1.println(" Hassan Akbar"); 
   outFile1.println(" CISC 3130");
   outFile1.println(" Professor Chuang");
   outFile1.println(" HW 1");
   outFile1.println();
     
     
  
     
   
   
    outFile1.println("Number of Songs Read in: " + songCount);
     
   outFile1.println("Number of Artists Read in: " + arrayOfArtists.size());
     
   outFile1.println("Total Views: " + totalViews);
   
   outFile1.println("Number of Errors: " + problemEntries);
     
   outFile1.println();
     
   outFile1.printf("%-25s %-25s %-25s", "Artist Name","Times Appeared","Artist Views");
     
   outFile1.println();
   
   
   
   
    for(int i=0; i < arrayOfArtists.size(); i++){
            outFile1.println( arrayOfArtists.get(i) );
        }
     
     
     
    outFile1.flush();
    outFile1.close();
     
     
    //close the output file
     
     
//*********************************************************************************    
    // sort the array in alphabetical order
    // could make this a method
    // bubble sort could use another sort
    // quicksort would be better
    // easier to sort the data before putting it in the list

    // will use compareToIgnoreCase
    // this is so a name that begins with lower case will be in proper alphabetical
    // order
    // other wise A to Z and then a-z will be the order
    // this is not intuitive for an alphabetical list
    
    // maybe use built in sort?
    
    // maybe another sort by times appeared or views
    // can I use an arraylist sort that ignores case?
    
    
    
    
    
    Artist copyArtist;
    
   
    
     for (int index = 0; index < arrayOfArtists.size(); index++){
       
      
        
      for (int j = 0; j < (arrayOfArtists.size() - 1) ; j++){
          
        if (arrayOfArtists.get(j+1).name.compareToIgnoreCase(arrayOfArtists.get(j).name) < 0) { 
            
          
          copyArtist = arrayOfArtists.get(j+1);
          
          // can make cleaner by using more tamp values
          // could use better sort
            
            
   
          
          arrayOfArtists.set(j+1, arrayOfArtists.get(j));
              
         
          
          arrayOfArtists.set(j, copyArtist);
              
        }
        
        
        
      }
     
           
    }
   
     
     
    
     
//*********************************************************************************     
   
    // printing to a different file than the unsorted arraylist
    
     
   
    PrintWriter outFile2 = new PrintWriter("myoutput2.txt");   // file
     
    outFile2.println(" Hassan Akbar"); // print info to output file
    outFile2.println(" CISC 3130");
    outFile2.println(" Professor Chuang");
    outFile2.println(" HW 1");
    outFile2.println();
     
    outFile2.println("Artist list in Alphabetical Order");
    
    
    outFile2.println("Number of Songs Read in: " + songCount);
     
   outFile2.println("Number of Artists Read in: " + arrayOfArtists.size());
     
   outFile2.println("Total Views: " + totalViews);
   
   outFile2.println("Number of Errors: " + problemEntries);
     
   outFile2.println();
     
   outFile2.printf("%-25s %-25s %-25s", "Artist Name","Times Appeared","Artist Views");
     
   outFile2.println();
     
  
    
     for(int i=0; i < arrayOfArtists.size(); i++){
            outFile2.println( arrayOfArtists.get(i) );
        }
     
     
    outFile2.flush();
    outFile2.close();
      
    
    
    
    
    
    
    
    
//*********************************************************************************
     
    System.out.println("********************************************"+
                       "********************************************");
    System.out.println("The program is terminating");
    System.out.println("********************************************"+
                       "********************************************");
    // outputs to the screen the program has finished
     
 }
 

     
//*********************************************************************************
 
}
