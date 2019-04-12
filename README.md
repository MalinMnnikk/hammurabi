# Overview

**The Hammurabi Project** aims to create a large-scale repository of computable law. Using a specially-designed Python library, we want to codify law in machine-executable form, in one giant "rulebase," encompassing as much law as will fit.

## Motivation

There are **millions of pages of law** - constitutions, statutes, regulations, case law, and interpretive decisions - with which citizens are expected to comply. This mass of material is logically complicated, difficult to contextualize, and based on an inaccessible vocabulary. Aside from the ethical issues caused by this complexity, it is grossly inefficient as an information system. The capital required for someone to understand a legal right or obligation is a wasted resource that creates drag on individual, corporate, and social progress.

Though not often thought of this way, **law is inherently computational**. It is a set of algorithms that prescribe how various computations are to be carried out. What is my standard (tax) deduction? Am I eligible for family and medical leave? On what day did I become liable for unemployment taxes? Determinations such as these are like mathematical functions: given various inputs, they produce corresponding outputs.  

This is not to say that the law is entirely mechanical. It's not. It's rife with vagueness, ambiguity, and inconsistency.  However, a large part of what makes the law inaccessible is its logical complexity: the way different facts and concepts relate to each other. And this aspect of law can (and has) been represented computationally.

The Hammurabi Project provides a vehicle for representing portions of the law in the Python programming language, so that the process of logical inference can be offloaded from human to machine. Once executable, it can be embedded into our computing infrastructure where it can drive other applications.

## Project Scope

Hammurabi's purpose is to make law-related determinations - that is, to apply legal rules to a given factual situation and report the result. The repository is set up to accept law from any jurisdiction in the world, but with a practical focus on English-language legal materials and U.S. law specifically.

U.S sources of legal rules include: the U.S. Code, Code of Federal Regulations, federal and state case law, state stautes and regulations, Executive Orders, and IRS publications, among other sources. Rules from one of these sources tend to reference those of other sources. Hammurabi weaves all of these sources together in a single, integrated knowledge base capable of deep legal analysis.

## Uses

Hammurabi might someday be used as:

* The back end of a system that dynamically interviews users to help them answer basic legal questions.
* The logic engine of a web service API that helps other computer systems process data about specific transactions.
* A business logic component of an enterprise IT system, to help keep that organization in compliance with the law.
* A way for government agencies to publish authoritative, machine-executable versions of the law.
* The core reasoning module of consumer legal apps.
* A policy simulation engine to experiment with the effects of hypothetical legal rules.

# Getting Involved

This is obviously a very ambitious vision, one that will take years and many, many people to build and maintain. At present, we are laying the groundwork for that vision. We're looking for lawyers, programmers, testers, writers, and app developers to help us achieve it.

## How You Can Help

- Build out a rule set in Python
- Write a specification page for a new rule set
- Create test cases 
- Help build other components of the Hammurabi ecosystem
- Donate
- Spread the word 

## Current Project Focus

While we welcome contributions on any legal topic, our initial focus will be on data privacy laws from around the world. Please see our data privacy portal for more information on this effort and how you can participate.

## More Information

Please see the project wiki for more information on this project.

# Legal

## Disclaimer

We are in the early stages of building Hammurabi. It is currently an experimental project that attempts to see what's possible, and not necessarily something that's ready for consumption by the public or an external information system.

**AT PRESENT, THE HAMMURABI PROJECT SHOULD NOT BE USED TO PROVIDE LEGAL INFORMATION TO CONSUMERS.**

When specific rule sets become mature enough to be released to the public, we will make that clear in our documentation.

## License

The code in this repository is subject to a modified version of the MIT license. (The last paragraph was added to the standard MIT license.)

> Copyright (c) 2011-2019 Foundation for Computable Law
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
> 
> NO REPRESENTATION OR WARRANTY IS MADE THAT THIS PROGRAM ACCURATELY REFLECTS
OR EMBODIES ANY APPLICABLE LAWS, REGULATIONS, RULES, OR EXECUTIVE ORDERS 
("LAWS"). YOU SHOULD RELY ONLY ON OFFICIAL VERSIONS OF LAWS PUBLISHED BY THE 
RELEVANT GOVERNMENT AUTHORITY, AND YOU ASSUME THE RESPONSIBILITY OF 
INDEPENDENTLY VERIFYING SUCH LAWS. THE USE OF THIS PROGRAM IS NOT A 
SUBSTITUTE FOR THE ADVICE OF AN ATTORNEY.
