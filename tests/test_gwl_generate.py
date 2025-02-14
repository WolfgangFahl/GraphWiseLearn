'''
Created on 14.02.2025

@author: wf
'''
from ngwidgets.basetest import Basetest
from ngwidgets.llm import LLM
from graphwiselearn.gwl_generate import ContentGenerator


class TestContentGenerator(Basetest):
    """
    test ContentGenerator
    """

    def setUp(self, debug=True, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.llm=LLM()

    def test_content_generator(self):
        content="""== Teaching Mathematical Concepts: Theory vs Examples ==

=== Example-First Approach: The 13-Knot Rope ===
Let's start with an ancient tool still relevant today:
* Take a rope with 13 equally spaced knots
* Form a triangle by:
** Using 3 segments between knots for first side
** Using 4 segments between knots for second side
** The remaining 5 segments form the longest side
* This automatically creates a right angle!
* Count the squares: <math>3^2 + 4^2 = 5^2</math>
* Observe: 9 + 16 = 25

'''Historical Note:''' This method was used by:
* Ancient Egyptian rope-stretchers (harpedonaptai)
* Medieval builders for squaring corners
* Modern-day gardeners and craftspeople

=== From Rope to Theory ===
After students physically create the triangle, we can show:
* Why it works: <math>a^2 + b^2 = c^2</math>
* More examples:
** 6-8-10 triangle (<math>36 + 64 = 100</math>)
** 5-12-13 triangle (<math>25 + 144 = 169</math>)

=== Theory Approach ===
The traditional theory-first approach would start with:
* The Pythagorean Theorem: "The square of the hypotenuse equals the sum of squares of the other two sides"
* The formula: <math>a^2 + b^2 = c^2</math>
* Then move to examples for verification

=== Teaching Recommendations ===
# For beginners:
#* Start with actual rope demonstration
#* Let them create the triangle
#* Count knot segments
#* Introduce formula last

# For advanced students:
#* Present theorem
#* Prove it
#* Use rope as practical validation

The key difference: Starting with a hands-on tool (13-knot rope) makes the abstract theorem concrete and memorable.

'''Activity Suggestion:''' Have students create their own 13-knot ropes using string and compare the accuracy of their right angles with a modern carpenter's square.
{{LLMHint}}
"""
        profile = "I am 13 year old student from London - my hobbies are soccer and badminton"
        # Test prompt generation
        generator = ContentGenerator(self.llm)

        prompt = generator.get_prompt(content, profile)
        if self.debug:
            print(prompt)
        self.assertTrue(len(prompt) > len(content))
        self.assertTrue("soccer" in prompt)

        # Test content generation if LLM is available
        if self.llm.available():
            result = generator.generate(content, profile)
            self.assertTrue(result is not None)
            if self.debug:
                print(result)