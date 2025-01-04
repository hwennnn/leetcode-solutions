---
title: Pub-sub Messaging
tags:
  - backend
date: 2025-01-05
---

## What is pub/sub messaging?

Publish-subscribe messaging, or pub/sub messaging, is an asynchronous communication model that makes it easy for developers to build highly functional and architecturally complex applications in the cloud. In modern cloud architecture, applications are decoupled into smaller, independent building blocks called *services*. Pub/sub messaging provides instant event notifications for these distributed systems. It supports scalable and reliable communication between independent software modules.

## How does pub/sub messaging work?

The publish-subscribe (pub/sub) system has four key components.

### **Messages**

A message is communication data sent from sender to receiver. Message data types can be anything from strings to complex objects representing text, video, sensor data, audio, or other digital content.

### **Topics**

Every message has a topic associated with it. The topic acts like an intermediary channel between senders and receivers. It maintains a list of receivers who are interested in messages about that topic.

### **Subscribers**

A subscriber is the message recipient. Subscribers have to register (or subscribe) to topics of interest. They can perform different functions or do something different with the message in parallel.

### **Publishers**

The publisher is the component that sends messages. It creates messages about a topic and sends them once only to all subscribers of that topic. This interaction between the publisher and subscribers is a one-to-many relationship. The publisher doesn’t need to know who is using the information it is broadcasting, and the subscribers don’t need to know where the message comes from.

![messaging topic](https://d1.awsstatic.com/product-marketing/Messaging/sns_img_topic.e024462ec88e79ed63d690a2eed6e050e33fb36f.png)

## What are the features of a pub/sub messaging system?

Applications developed with a publish-subscribe (pub/sub) pattern have separate application and communication logic. The messaging infrastructure decouples message delivery between publishers and subscribers and broadcasts to different subscribers asynchronously.

The pub/sub communication system has the following key features.

### **Push delivery**

Pub/sub messaging instantly pushes asynchronous event notifications when messages are published to the message topic. Subscribers are notified when a message is available.

### **Multiple delivery protocols**

Topics connect to multiple types of endpoints, such as message queues, serverless functions, HTTP servers, and email addresses.

[Read about message queueing with AWS »](https://aws.amazon.com/sqs/)

### **Fanout**

This scenario happens when a message is sent to a topic and then replicated and pushed to multiple endpoints. Fanout provides asynchronous event notifications, which in turn allow for parallel processing.

### **Filtering**

The filtering feature empowers the subscriber to create a message filtering policy. So, they’ll only get the notifications they’re interested in, as opposed to receiving every single message posted to the topic.

### **Multiplexing**

In some cases, publishers can also be subscribers. You can multiplex message streams and create systems that link together in an internally consistent manner.

## What are the benefits of pub/sub messaging?

The publish-subscribe (pub/sub) model enables [event-driven architecture](https://aws.amazon.com/event-driven-architecture/), which is required in several modern applications. You can use events to trigger and communicate between decoupled services. An event is a change in state, or an update, like an item being placed in a shopping cart.

Pub/sub messaging provides significant advantages to developers who build applications that rely on real-time events. We outline some of the advantages below.

### **Eliminate polling**

Message topics allow instantaneous, push-based delivery, eliminating the need for message consumers to periodically check, or poll, for new information and updates. This promotes faster response time and reduces the delivery latency that can be particularly problematic in systems where delays cannot be tolerated.

### **Dynamic targeting**

The pub/sub pattern makes the discovery of services easier, more natural, and less error-prone. Instead of maintaining a roster of peers so an application can send messages, a publisher will simply post messages to a topic. Then, any interested party will subscribe its endpoint to the topic and start receiving these messages. Multiple subscribers can change, upgrade, or disappear, and the system adjusts dynamically.

### **Decouple and scale independently**

Pub/sub makes the software more flexible. Publishers and subscribers are decoupled and work independently from each other, which allows you to develop and scale them independently. You can decide to handle orders one way this month and then another the following month. Adding or changing functionality won’t send ripple effects across the system, because pub/sub allows you to flex how everything works together.

### **Simplify communication**

Code for communications and integration is some of the hardest code to write. The publish-subscribe model reduces complexity by removing all the point-to-point connections with a single connection to a message topic. The topic will manage subscriptions to decide what messages should be delivered to which endpoints. Fewer callbacks result in looser coupling, plus code that is easier to maintain and extend.

### **Durability**

Pub/sub messaging services often provide very high durability, and at-least-once delivery, by storing copies of the same message on multiple servers.

### **Security**

Message topics authenticate applications that try to publish content and allow you to use encrypted endpoints to secure messages in transit over the network.

## What are the use cases of pub/sub messaging?

We outline popular use cases of the publish-subscribe (pub/sub) messaging system below.

### **Perform parallel asynchronous processing**

Events published to a message topic can trigger multiple workers to perform necessary but unrelated tasks simultaneously.

### **Deliver application and system alerts**

Instantly deliver critical updates and asynchronous event notifications to affected application components and your users.

### **Manage asynchronous workflows**

Relay events among applications, move data between data stores, refresh distributed caches, or update records in business systems.

### **Balance workloads**

Batch up tasks for bulk processing, or break up a larger task into many smaller ones and use message queuing to divide the work among multiple workers.

### **Log to multiple systems**

Record events to analyze later, capture logs for operations and security, or archive to meet backup or compliance requirements.

### **Use fanout for replication**

Replicate data between production and development environments, or develop and test with live data.

### **Coordinate serverless applications**

Fanout asynchronous event notifications to distributed functions and message queues to coordinate the components of your serverless application.

### **Stream IoT Data**

The pub/sub pattern is a very powerful way for Internet of Things (IoT) devices to interact. Devices can easily stream data to backend systems or each other.

## What is the difference between message queues and pub/sub messaging?

A [message queue](https://aws.amazon.com/message-queue/) is another form of asynchronous communication used in serverless and [microservices](https://aws.amazon.com/microservices/) architectures. Messages are stored in the queue until they are processed and deleted. Message queues require the sender to know who they are exchanging messages with. Message ordering may also cause bottlenecks in the system.

In contrast, the publish-subscribe (pub/sub) pattern allows for more flexibility. Several interested subscribers can receive messages simultaneously and asynchronously. Publishers don't need to know who the subscribers are. Message handling is more scalable and reliable, and it gives better performance.
