#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def ipChecker(self, ips, pattern):
        """
        : ips: List[Str] candidate ips
        : pattern: legal ip pattern
        : return: List[Str] valid ips
        """
        # how will the valid pattern be like
        # what's the point of this question
        iplen = 4
        res = []
        parsedPattern = pattern.split('.')
        for i, x in enumerate(parsedPattern):
            parsedPattern[i] = x.split('/')

        for ip in ips:
            parsedIp = ip.split('.')
            if len(parsedIp) != iplen:
                continue
            for i in range(iplen):
                if len(parsedPattern[i]) == 1:
                    pass
                elif len(parsedPattern[i]) == 2:
                    pass

        return res

if __name__ == '__main__':
    s = Solution()
    ipsTests = [[], ['1.0.0.0', '1.0.0.1', '1.0.0.0.9']]
    patterns = ['', '1.0.0.0/9']

    for ips, p in zip(ipsTests, patterns):
        print s.ipChecker(ips, p)
