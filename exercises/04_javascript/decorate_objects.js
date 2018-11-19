function addPersonMethods(person){
this.name = person.name;
this.age = person.age;

person.greet = function (sentence){
return sentence + ", my name is " + person.name;
};

person.compareAge = function(person){
  if (this.age < person.age)
  {
  return "My name is " + this.name + " and I'm younger than " +person.name
  }
  if(this.age == person.age)
  {
  return ["My name is " +this.name + " and I'm as young as " +person.name].join("");
  }
  else
  {
  return ["My name is " +this.name + " and I'm older than " +person.name].join("");
  }
};

person.namesake = function(person){
  if(this.name == person.name)
  {
  return ["We have the same name, " + person.name + " and I!"].join("");
  }
  else
  {
  return ["We have different names, " + person.name + " and I."].join("");
  }
};


return person;
}
