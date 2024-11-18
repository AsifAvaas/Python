import requests

def postReview():
    comment=input("Enter the review: ")
    id=input("Enter your userId: ")
    id= id or "66e68c5942494f1bb6813b6d"
    email=input("Enter your email address: ")
    postReview= requests.post('https://vivisteria-2lrx.vercel.app/api/review',json={'comment':comment,'userId':id,'email':email})


def getReviews():
    datainfo=requests.post('https://vivisteria-2lrx.vercel.app/api/displayreviews')
    data=datainfo.json()

    for line in data:
        print(line['_id'],line['comment'])


while True:
    print("Press 1 to write a review: ")
    print("Press 2 to read all the reviews: ")
    print("Press 3 to exit: ")
    choice=int(input("Enter: "))

    if choice==1:
        postReview()
    elif choice==2:
        getReviews()
    else:
        print("Thank you")
        break
