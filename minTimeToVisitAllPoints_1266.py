points = [[1,1],[3,4],[-1,0]]

def minTimeToVisitAllPoints(points):
    res = 0
    x1, y1 = points.pop()  # শেষ পয়েন্টটা নিচ্ছি

    while points:
        x2, y2 = points.pop()  # পরবর্তী পয়েন্ট নিচ্ছি
        res += max(abs(x1 - x2), abs(y1 - y2))  # Chebyshev Distance যোগ করছি
        x1, y1 = x2, y2  # নতুন স্টার্ট পয়েন্ট সেট করছি
    return res
print(minTimeToVisitAllPoints(points))