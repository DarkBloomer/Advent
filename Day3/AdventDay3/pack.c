#include <iostream>
#include <map>
#include <typeinfo>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

//take input and create a vector of strings
vector<string> readFile(string input) {

	ifstream inputFile(input);

	//check if file was opened correctly
	if (!inputFile.is_open()) {
		cerr << "Error: Could not open file" << endl;
	}		

	//Read the file line by line
	string line;

	//store contents of packs in vector
	vector<string> packs;

	while (getline(inputFile, line)) {
		//add lines to vector
		packs.push_back(line);
	}

	//Close the file
	inputFile.close();

	return packs;
} 	


int findPrior(char c) {
	int prior = int(c);

	if(isupper(c)) {
		prior = prior - 38;	
	}

	else{
		prior = prior - 96;
	}

	return prior;
}

//finds the duplicate char in two strings
char findDups(string str1, string str2){
	char dup;

	for(int i = 0; i < str1.size(); i++) {
		for(int j = 0; j < str2.size(); j++) {
			if(str1.at(i) == str2.at(j)){
				dup = str1.at(i);
			}
		}
	}

	return dup;
}

char dup(string contents) {
	//find length of string
	int len = contents.size();

	//find first half of string
	string first = contents.substr(0, (len / 2));

	//find second half of string
	string second = contents.substr((len / 2), contents.size() - 1);

	//find the common char between first and second
	char dup = findDups(first, second);

	return dup;
}




int main () {
	//stores contents of each elf pack
 	vector<string> elfPacks;

	elfPacks = readFile("input.txt"); 

	//find the sum of all duplicates
	int dupSum = 0;

	//vector for all groups
	vector<vector<string>> groups;

	//vector to hold a single group
	vector<string> g;

	//flag to signal when a group has been formed
	int flag = 0;

	for(int i = 0; i < elfPacks.size(); i++){

		//find duplicate word
		char duplicate = dup(elfPacks[i]);

		//find priority associated with duplicate
		int prior = findPrior(duplicate);

		//add priority to duplicate sum
		dupSum += prior;

		//create groups for finding triplets in groups
		g.push_back(elfPacks[i]);
		flag++;

		if(flag == 3) {
			groups.push_back(g);
			g.clear();
			flag = 0;	
		}		

	}

	
	map<int, char> trips;
	for(int k = 0; k < groups.size(); k++){
		string fir = groups.at(k).at(0);
		string sec = groups.at(k).at(1);
		string thir = groups.at(k).at(2);

		bool flag = true;
		//loop through first string in the group	
		for(int z = 0; z < fir.size(); z++){
			
			//loop through second string in the group
			for(int l = 0; l < sec.size(); l++){

				//loop through third string in the group
				for(int q = 0; q < thir.size(); q++) {

					if(fir[z] == sec[l] && sec[l] == thir[q] && thir[q] == fir[z] && trips.count(k) == 0){
						trips[k] = fir[z];
					}
				}
			}
		}
	}
		

	map<int, char>::iterator itr;
	int tripSum = 0;
    	for(itr=trips.begin();itr!=trips.end();itr++){
   		int pri = findPrior(itr->second); 
		tripSum += pri;
   	} 
	
	//print results
	cout << "Size of groups: " + to_string(groups.size()) << endl;
	cout << "size of elfPacks: " + to_string(elfPacks.size()) << endl;
	cout << "Sum of duplicates: " + to_string(dupSum) << endl;
	cout << "Sum of triplets: " + to_string(tripSum) << endl;

	return 0;
}
