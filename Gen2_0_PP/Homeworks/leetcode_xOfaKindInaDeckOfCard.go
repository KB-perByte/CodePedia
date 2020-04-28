//https://leetcode.com/submissions/detail/331409187/
package main

import "math"

func hasGroupsSizeX(deck []int) bool {
	occ := map[int]int{}

	for _, i := range deck {
		occ[i]++
	}
	min := math.MaxInt32

	for _, rec := range occ {
		if min == math.MaxInt32 {
			min = rec
		} else {
			min = cal_gcd(min, rec)
		}
		if min < 2 {
			return false
		}
	}
	return true
}

func cal_gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return cal_gcd(b, a%b)
}
