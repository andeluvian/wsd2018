function addPersonMethods(person){
this.name = person.name;
this.age = person.age;

person.greet = function (sentence){
console.log(sentence + ", my name is " + person.name);
};

person.compareAge = function(person){
  if (this.age < person.age)
  {
  console.log(["My name is " + this.name + " and I'm younger than " +person.name].join(""));
  }
  if(this.age == person.age)
  {
  console.log(["My name is " +this.name + " and I'm equally young as " +person.name].join(""));;
  }
  if(this.age > person.age)
  {
  console.log(["My name is " +this.name + " and I'm older than " +person.name].join(""));;
  }
};

person.namesake = function(person){
  if(this.name == person.name)
  {
  console.log(["We have the same name, " + person.name + " and I!"].join(""));
  }
  else
  {
  console.log(["We have different names, " + person.name + " and I."].join(""));
  }
};



return person;
}
