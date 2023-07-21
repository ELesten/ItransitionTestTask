# ItransitionTestTask
Task 1

Implement the function to find the combination of 4 digits in a row which gives the max multiplication. If
object is not a string or there are no combinations found - return nil. If combination is found - return it&#39;s
multiplication result.
E.g.
max_multiplication(&#39;abc12345def&#39;) =&gt; 120  # 2*3*4*5
max_multiplication(&#39;a1b2c3d4e&#39;) =&gt; nil

Task 2

Implement the function to sort array of numbers by amount of &#39;1&#39; in its binary representation. Numbers
with identical amount of &#39;1&#39;s should be ordered by decimal representation.
E.g.
 3 = 11, 7 = 111, 8 = 1000, 9 = 1001.
sort([3,7,8,9]) =&gt; [8,3,9,7]  # 1000, 11, 1001, 111
