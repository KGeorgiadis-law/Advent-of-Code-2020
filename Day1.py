# Day 1

input_string = """
1597
1857
1703
1956
1809
1683
1629
230
1699
1875
1564
1700
1911
1776
1955
1585
1858
1725
1813
1568
1962
1535
487
1621
1620
1573
1918
1794
2003
1957
1840
1936
285
1630
1753
1649
1951
1968
1916
1694
1593
1980
1806
1779
1637
1674
1842
1659
1553
1846
1677
1944
1811
1645
1784
1791
1988
1864
1596
1773
1132
1715
1938
1901
1617
1892
1708
1788
1765
1684
1595
1971
1798
1543
507
1772
1757
1950
1844
1898
1671
1602
1599
1524
2005
1855
1624
1884
1990
1604
1873
1736
1747
1900
1534
1713
1690
1525
1838
587
74
1979
1635
1896
1580
1727
1994
1940
1819
1758
1852
1639
1754
1559
1919
1879
1874
1921
1575
1693
1710
1949
1719
1933
1673
1909
1989
1897
909
1889
1641
1658
1530
1541
1952
1627
1839
1803
833
1527
1756
2009
1605
1548
1660
1966
1770
1552
1939
1726
382
1665
1960
1733
1983
1544
1974
1985
1625
609
1931
1749
1975
1562
1563
1922
2008
2010
1704
1545
1636
1762
1841
1717
622
2007
1670
1771
1910
1978
1615
1805
1999
1643
1748
1531
1539
1787
1722
1111
1774
1540
1607
1902
1991
1763
1691
1812
1783
1579
"""

# convert string to a list of answers
num_array = [int(v) for v in input_string.split("\n") if v != ""]


def first_problem(num_array):
    for n in num_array:
        first_number = n
        second_number = 2020 - n
        if (second_number) in num_array:
            return (first_number * second_number)


def second_problem(num_array):
    '''this is an example of the 3SUM problem. 
  You can read about it here:
  https://en.wikipedia.org/wiki/3SUM and
  https://www.tutorialspoint.com/3sum-in-python
  I'm afraid I couldn't figure this out on my own 
  so I just copied the solution from the second link!
  '''
    num_array.sort()
    result = []
    for i in range(len(num_array) - 2):
        if i > 0 and num_array[i] == num_array[i - 1]:
            continue
        l = i + 1
        r = len(num_array) - 1
        while (l < r):
            sum = num_array[i] + num_array[l] + num_array[r]
            if sum < 2020:
                l += 1
            elif sum > 2020:
                r -= 1
            else:
                result.append([num_array[i] * num_array[l] * num_array[r]])
                while l < len(num_array) - 1 and num_array[l] == num_array[l +1]:
                    l += 1
                while r > 0 and num_array[r] == num_array[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return result
