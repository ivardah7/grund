def get_tempatures() : 
    get_tempatures = [7, 9, 13, 21, 19, -3, 2, ]
    print(len(get_tempatures))
    print(sum(get_tempatures))
    print(min(get_tempatures))
    print(max(get_tempatures))
    average = sum(get_tempatures) / len(get_tempatures)
    print("Medeltempratur", average)
    
    print("Tempraturer högre än medeltempraturen")
    for tempature in get_tempatures:
        if tempature > average: 
            print(tempature)