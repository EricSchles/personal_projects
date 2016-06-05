#include <iostream>
using namespace std;

class Node{
public:
  int data;
  Node *next;
  Node(int data, Node *next){
    this->data = data;
    this->next = next;
  }
  void pprint(){ cout << this->data << endl; }
};

class LinkedList{
public:
  Node *head;
  int size;
  LinkedList(){
    this->head = new Node(-1,NULL);
    this->size = 0;
  }
  void append(int data);
  void pprint();
  void remove_by_value(int data);
};

void LinkedList::append(int data)
{
  Node *cur = this->head;
  int counter = 0;
  while(cur->next != NULL){
    cur = cur->next;
  }
  Node *newNode = new Node(data,NULL);
  cur->next = newNode;
  this->size++;
}

void LinkedList::pprint(){
  Node *cur = this->head;
  cur = cur->next;
  while (cur != NULL){
    cout << cur->data << endl;
    cur = cur->next;
  }
}

void remove_node(int current_index){

}

void LinkedList::remove_by_value(int data){
  //cpp is lame, I should totally implement a smart list :) (what I'm doing now)
  int arr[this->size];
  int current_index = 0;
  Node *cur = this->head;
  int counter = 0;
  cur = cur->next; //skipping the head pointer
  while (cur != NULL){
    if ( cur->data == data){
      arr[current_index] = counter;
      current_index++;  
    }
    counter++;
  }
  for(int i = 0; i < this->size; i++){
    //do removing here
    //consider offloading this to a method
  }
  
}
int main()
{
  //Node *head = new Node(5,NULL);
  //head->pprint();
  /*
  LinkedList *ll = new LinkedList();
  ll->append(5);
  ll->append(7);
  ll->append(9);
  ll->pprint();
  */
  //LinkedList ll;
  //ll.append(5);
  /* 
  //works
  Node *head = new Node(0,NULL);
  Node *cur = head;

  //appending values
  for ( int i = 0; i < 10; i++){
    Node *tmp = new Node(i,NULL);
    cur->next = tmp;
    cur = cur->next;
  }
  cur = head;
  while(cur != NULL){
    cout << cur->data << endl;
    cur = cur->next;
    }*/
  return 0;
}
