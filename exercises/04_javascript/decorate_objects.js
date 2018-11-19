function addPersonMethods(person){

var person = {};
person.name = name;
person.age = age;

console.log('Hi! I\'m ' + this.name + '.');

};

function greet(sentence)
{
return sentence + ", my name is " + this.name
}

function compareage(anotherPersonObject){

if (this.age < anotherPersonObject.age)
{
return "My name is " + this.name + " and I'm younger than " +anotherPersonObject.name
}
if(this.age == anotherPersonObject.age)
{
return "My name is " +this.name + " and I'm as young as " +anotherPersonObject.name
}
else
{
return "My name is " +this.name + " and I'm older than " +anotherPersonObject.name
}
}

function namesake(anotherPersonObject){

if(this.name == anotherPersonObject.name){

  return "We have the same name, " + anotherPersonObject.name + " and I!"
}
else
{
  return "We have different names, " + anotherPersonObject.name + " and I."
}

}
