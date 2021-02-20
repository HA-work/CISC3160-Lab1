#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

// This is a code that uses a greedy approach to maximize a schedule
// It is assumed that the outcome that is desired is the maximum number of
// activities that do not conflict are to be selected





// This is an activity object

struct Activity
{
    double start, finish;



    string name;

    //int activityNum; // not really as important as the other info


    int startHour = (int)start;

    int startMin = (int)round(((start -(int)start) * 100));

    int finishHour = (int)finish;

    int finishMin =  (int)round(((finish -(int)finish) * 100));


// the second typecast might be unnessecary for mins
// also unnesecary for Hour but good to be explicit

//	time might have been a better class to use
// calendar object is another possibility

// this method fixes any rounding errors caused





    int duration = 60*(finishHour - startHour) + (finishMin - startMin);

    int intersections = 0;






    string toString()const
    {



        string temp = name + "(" + to_string(startHour) + ":" ;


        if (startMin < 10)
        {

            temp = temp + "0" + to_string(startMin);


        }
        else
        {

            temp = temp + to_string(startMin);


        }



        temp = temp +   "-" + to_string(finishHour) + ":" ;





        if (finishMin < 10)
        {

            temp = temp + "0" + to_string(finishMin);


        }
        else
        {

            temp = temp + to_string(finishMin);


        }



        temp = temp + ")";

        temp = temp + " " + to_string(duration) + " minutes" + " / ";


        temp = temp + " " + to_string(intersections) + " intersections";


        // could format the string better



        return temp;


    }






};




bool activityCompare(Activity& s1, Activity& s2)
{
    return (s1.finish < s2.finish);




    // for start early use start here

//	return (s1.start < s2.start);
    // has the issue of only taking the first start early available when others may be better


    // for the other 2 need to find a way to compare what is being added to everything already added to the new
    // array to check for intersections



}

// Returns count of the maximum set of activities that can
// be done by a single person, one at a time.

// add to an array? or vector?


void mergeV(vector<Activity>& arr, int l, int m, int r)  // need to remember to pass a refrence to the vector
{
    // need to pass a reference to the vector with &
    // if you do not only the copy is sorted


    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temp arrays
    vector<Activity> L(n1), R(n2);



    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
    {
        L[i] = arr[l + i];
    }
    for (int j = 0; j < n2; j++)
    {
        R[j] = arr[m + 1 + j];
    }

    // Merge the temp arrays back into arr[l..r]

    // Initial index of first subarray
    int i = 0;

    // Initial index of second subarray
    int j = 0;

    // Initial index of merged subarray
    int k = l;

    while (i < n1 && j < n2)
    {
        if (L[i].finish <= R[j].finish)
        {
            arr[k] = L[i];
            i++;




        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of
    // L[], if there are any
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of
    // R[], if there are any
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}













void mergeSort(vector<Activity>& arr, int l, int r)
{

    // need to remember to pass a refrence to the vector with &
    // if you do not only the copy is sorted



//
    int m;
    if(l < r)
    {
        int m = (l+r)/2;
        // Sort first and second arrays
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        mergeV(arr, l, m, r);
    }
}



void printMaxActivities(vector<Activity>& arr)
{

    // need to pass a refrence to the vector with &
    // if you do not only the copy is sorted

    // created my own merge sort
    // could use library sort
    // not sure how it would work with a user defined type though





//     Sort jobs according to finish time
    //sort(arr.begin(), arr.end(), activityCompare);

    mergeSort(arr, 0, arr.size()-1);








    cout << "Following activities are selected "<< endl << endl;

    // The first activity always gets selected
    int i = 0;

    int m = 1; // number in the new schedule

    int time = 0;

    cout << m << " " << arr[i].toString() << endl;

    time = time + arr[i].duration;

    // Consider rest of the activities
    for (int j = 1; j < arr.size(); j++)
    {
        // If this activity has start time greater than or
        // equal to the finish time of previously selected
        // activity, then select it
        if (arr[j].start >= arr[i].finish)
        {


            m++;
            cout << m << " " << arr[j].toString() << endl;
            i = j;

            time = time + arr[i].duration;

// instead of printing could move to another vector for optimized schedule

        }
    }

    cout   << endl;

    cout << "The number of activities is: " << m  << endl;

    cout << "The total time spent is: " << time << " minutes" << endl;

}

// Driver program
int main()
{

    //vector would be better
    // would be better if could read these values in from the excel or csv file




    vector<Activity> sched = {{6, 6.10, "Meditation" },
        {6.05, 6.30, "Shower" },
        {6.08, 6.12, "Bathroom Break 1"},
        {6.25, 7, "Running" },
        {6.35, 7.4, "Biking" },
        {6.45, 8, "Elliptical" },
        {7.55, 9.30, "Fencing" },
        {8, 10, "Polo" },
        {8, 9.30, "Reading" },
        {9.20, 9.35, "Squats" },
        {9.30, 9.40, "Pushups" },
        {9.45, 10.15, "Cardio Workout" },
        {10,11, "Learning Python" },
        {10, 10.05, "Bathroom Break 2" },
        {10.30, 14.30, "Skydiving" },
        {10.30, 12, "Open CV class" },
        {11, 13.30, "Algorithms class" },
        {13, 13.30, "Going out for ice cream" },
        {13, 14.30, "Going out for burgers" },
        {13,16, "barbecue" },
        {14,16, "Gardening" },
        {14.05, 14.09, "Bathroom Break 3" },
        {15,17, "Driving lessons" },
        {15,17.30, "Home Repairs" },
        {16,18, "Mock interviews" },
        {16,17, "Laundry" },
        {16.01, 16.05, "Bathroom Break 4" },
        {17,19, "Resume improvement" },
        {17,20, "Gift Shopping" },
        {18,21, "Netflix" },
        {18.30, 21.10, "Taking a test" },
        {19,20, "Culinary Course" },
        {19,20, "Piano" },
        {19.01, 19.05, "Bathroom Break 5" },
        {19.30, 20.30, "Guitar " },
        {21,21.30, "Foreign language lesson" }
    };


// there could be a better way to enter the times
// maybe make use of calendar class?
// that works for java but what about c++

















    for (int i = 0; i< sched.size() ; ++i)
    {


        for (int j = 0; j< sched.size(); ++j)
        {


            if(i!=j)
            {
// .at would be better

                if((sched[i].start >= sched[j].start && sched[i].start < sched[j].finish) ||
                        (sched[i].finish > sched[j].start && sched[i].finish <= sched[j].finish) ||
                        (sched[i].start <= sched[j].start && sched[i].finish >= sched[j].finish)||
                        (sched[i].start >= sched[j].start && sched[i].finish <= sched[j].finish))
                {

                    // the last condition should be unneeded but is a good safeguard



                    // should add for if one engulfs the other
                    // could add another for fits inside but I beleive it is already satisfied by the first 2 conditions

                    sched[i].intersections++;

                }







            }


        }


    }




    //int n = sizeof(arr)/sizeof(arr[0]);

    int m = sched.size();

    //printMaxActivities(arr, n);


    // better to sort here


    printMaxActivities(sched);









    return 0;
}

/*


Following activities are selected

1 Meditation(6:00-6:10) 10 minutes /  2 intersections
2 Running(6:25-7:00) 35 minutes /  3 intersections
3 Fencing(7:55-9:30) 95 minutes /  4 intersections
4 Pushups(9:30-9:40) 10 minutes /  2 intersections
5 Bathroom Break 2(10:00-10:05) 5 minutes /  2 intersections
6 Open CV class(10:30-12:00) 90 minutes /  3 intersections
7 Going out for ice cream(13:00-13:30) 30 minutes /  4 intersections
8 Bathroom Break 3(14:05-14:09) 4 minutes /  4 intersections
9 Bathroom Break 4(16:01-16:05) 4 minutes /  4 intersections
10 Resume improvement(17:00-19:00) 120 minutes /  5 intersections
11 Bathroom Break 5(19:01-19:05) 4 minutes /  5 intersections
12 Guitar (19:30-20:30) 60 minutes /  5 intersections
13 Foreign language lesson(21:00-21:30) 30 minutes /  1 intersections

The number of activities is: 13
The total time spent is: 497 minutes



*/


