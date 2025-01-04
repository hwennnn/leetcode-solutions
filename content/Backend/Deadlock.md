---
title: Deadlock
tags:
  - backend
date: 2025-01-05
---

### Four conditions for Deadlock

Deadlock in a system can occur when the following four conditions hold simultaneously:

- Mutual Exclusion: At least one resource must be held in a non-shareable mode; that is, only one process can use the resource at any given time. If another process requests that resource, the requesting process must be delayed until the resource has been released.
- Hold and Wait: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.
- No Preemption: Resources cannot be forcibly taken from a process holding them; they can only be released voluntarily by the process holding them, after that process has completed its task.
- Circular Wait: There must be a set of processes $P_1, P_2, \ldots, P_n$ such that $P_1$ is waiting for a resource that is held by $P_2, P_2$ is waiting for a resource that is held by $P_3, \ldots, and  \ P_n$ is waiting for a resource that is held by $P_1$, thus forming a circular chain of processes waiting for resources.

### Methods of Handling Deadlocks in Operating System

The first two methods are used to ensure the system never enters a deadlock.

#### Deadlock Prevention

This is done by restraining the ways a request can be made. Since deadlock occurs when all the above four conditions are met, we try to prevent any one of them, thus preventing a deadlock.

#### Deadlock Avoidance

When a process requests a resource, the deadlock avoidance algorithm examines the resource-allocation state. If allocating that resource sends the system into an unsafe state, the request is got granted.

Therefore, it requires additional information such as how many resources of each type is required by a process. If the system enters into an unsafe state, it has to take a step back to avoid deadlock.

#### Deadlock Detection and Recovery

We let the system fall into a deadlock and if it happens, we detect it using a detection algorithm and try to recover.

Some ways of recovery are as follows.

- Aborting all the deadlocked processes.
- Abort one process at a time until the system recovers from the deadlock.
- Resource Preemption :Resources are taken one by one from a process and assigned to higher priority processes until the deadlock is resolved.

#### Deadlock Ignorance

In the method, the system assumes that deadlock never occurs. Since the problem of deadlock situation is not frequent, some systems simply ignore it. Operating systems such as UNIX and Windows follow this approach. However, if a deadlock occurs we can reboot our system and the deadlock is resolved automatically.

**Note**: The above approach is an example of Ostrich Algorithm. It is a strategy of ignoring potential problems on the basis that they are extremely rare.
