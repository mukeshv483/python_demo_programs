first=input("enter number")
second=input("enter number")
third=input("enter number")
fourth=input("enter number")
if((first>second) and (first>third) and (first>fourth)):
     print("\nFirst number is largest");
elif((second>first) and (second>third) and (second>fourth)):
       print("\nSecond number is largest");
elif((third>second) and (third>first) and (third>fourth)):
    print("\nThird number is largest");
elif((fourth>second) and (fourth>third) and (fourth>first)):
    print("\nFourth number is largest");
if((first<second) and (first<third) and (first<fourth)):
   print("\nFirst number is smallest");
elif((second<first) and (second<third) and (second<fourth)):
    print("\nSecond number is smallest");
elif((third<second) and (third<first) and (third<fourth)):
     print("\nThird number is smallest");
elif((fourth<second) and (fourth<third) and (fourth<first)):
     print("\nFourth number is smallest");
