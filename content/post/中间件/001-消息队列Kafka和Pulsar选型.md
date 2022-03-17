---
title: "01-消息队列Kafka和Pulsar选型"
author: "lucas"
description: ""
date: 2022-03-17
lastmod: 2022-03-17

tags: ["MQ"]
categories: ["中间件"]
keywords: ["mq", "消息队列", "kafka", "pulsar"]
---

<div align="center"><font size=35>消息队列Kafka和Pulsar选型</font></div>

# Table of Contents

- [Table of Contents](#table-of-contents)
- [1: 业务场景](#1-业务场景)
  - [1.1 业务场景描述](#11-业务场景描述)
  - [1.2 业务场景 feature](#12-业务场景-feature)
- [2：消息中间件](#2消息中间件)
- [3: Kafka 特性](#3-kafka-特性)
- [4: Pulsar 特性](#4-pulsar-特性)
- [5: Kafka 和 Pulsar 对比](#5-kafka-和-pulsar-对比)

# 1: 业务场景

- https://mp.weixin.qq.com/s/K6xj4LfplB16Q_DfQL75PA

## 1.1 业务场景描述

- 我们需要一个把实时的交易数据进行持久化保存，并且能快速的给其他服务提供最新的交易数据;
- 当服务启动或者重启后，能快速提供完整的并且最新的交易数据;
- 现有的机制是每个订单使用 go 协程直接写入 Mysql 数据库,对数据库的压力比较大，且系统的延迟比较高;

## 1.2 业务场景 feature

- 解耦，降低数据数据库性能导致的整个服务延迟;
- 数据完整的，及时地进行持久化;
- 交易数据能，迅速的提供给其他需要数据的服务;
- 流量消峰，减少峰值流量直接对数据库服务造成的冲击, 提高系统的稳定性;

# 2：消息中间件

- 适合用消息中间件解决上述问题;
  - (1) **解耦:** 将一个流程的上游和下游拆开，上游专注生产消息，下游专注处理消息;
  - (2) **广播:** 一个上游生产的消息轻松被多个下游服务消费处理;
  - (3) **缓冲(流量削峰):** 如果上游服务流量突然暴涨,mq 可以做一个缓冲器的作用，下游根据消费能力对消息进行消费，避免暴涨的流量直接对下游服务造成冲击;
  - (4) **异步**: 生产者生产消息之后可以马上直接返回，消费者可以异步处理消息;
  - (5) **冗余**: 保留历史消息，处理失败或者当出现异常的时候可以进行重试或者回溯，防止消息丢失。
- 近几年出现了一些关注度较高的消息队列中间件选型，如 Kafka、Pulsar、RocketMQ 等，首先从宏观上做一些对比：
  <table border="3">
    <caption><font size="5" color="blue">常见MQ对比</font></caption>
  	<tr>
  	    <th>MQ</th>
  	    <th>特性</th>
  	    <th width="20px">描述</th>
  	    <th>Kafka</th>
  	    <th>Pulsar</th>
  	    <th>RocketMQ</th>
  	    <th>RabbitMQ</th>
  	    <th width="20px">NSQ</th>  
  	    <th>我们的业务场景是否需要</th>  
  	</tr>
    <tr >
        <td>推出时间</td>
        <td></td>
        <td></td>
        <td>2012 年(Scala 和 Java) </td>
        <td>2016 年(Java)</td>
        <td>2012 年(Java)</td>
        <td>2007 年(Erlang)</td>
        <td>2013 年(Go)</td>
        <td></td>
    </tr>
    <tr >
        <td>组织</td>
        <td></td>
        <td></td>
        <td>Linkin 开源，Apache </td>
        <td>Yahoo 开源，Apache </td>
        <td>阿里开源，Apache </td>
        <td>Pivotal 开源,Mozilla</td>
        <td>MIT</td>
        <td></td>
    </tr>
  	<tr >
  	    <td rowspan="13"><b>功能</b></td>
        <td><b>消费模式</b></td>
        <td>consumer消费消息的方式</td>
        <td>pull</td>
        <td>push</td>
        <td>pull</td>
        <td>push</td>
        <td>push</td>
        <td>?</td>
  	</tr>
  	<tr>
        <td><b>延迟队列</b></td>
        <td>消息投递延迟</td>
        <td><font color="red">No</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td></td>
  	</tr>
  	<tr>
        <td><b>死信队列</b></td>
        <td></td>
        <td><font color="red">No</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td>?</td>
  	</tr>
  	<tr>
        <td><b>优先级队列</b></td>
        <td></td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td></td>
  	</tr>
  	<tr>
        <td><b>消息回溯</b></td>
        <td></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td>需要</td>
  	</tr>
  	<tr>
        <td><b>消息持久化</b></td>
        <td></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td>需要</td>
  	</tr>
  	<tr>
        <td><b>消息确认机制</b></td>
        <td></td>
        <td>offset</td>
        <td>offset+单条</td>
        <td>offset</td>
        <td>单条</td>
        <td>单条</td>
        <td>需要</td>
  	</tr>
  	<tr>
        <td><b>消息TTL</b></td>
        <td>消息TTL表示一条消息的生存时间，如果消息发出来后，在TTL的时间内没有消费者进行消费，消息队列会将消息删除或者放入死信队列中</td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td>需要</td>
  	</tr>
  	<tr>
        <td><b>多租户隔离</b></td>
        <td></td>
        <td><font color="red">No</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td>?</td>
  	</tr>
  	<tr>
        <td><b>消息顺序性</b></td>
        <td>消息顺序性是指保证消息有序。消息消费顺序跟生产的顺序保持一致</td>
        <td>分区有序</td>
        <td>stream模式有序</td>
        <td>consumer加锁</td>
        <td><font color="red">No</font></td>
        <td><font color="red">No</font></td>
        <td>?</td>
  	</tr>
  	<tr>
        <td><b>消息查询</b></td>
        <td>查看MQ中消息的内容，比如通过某个MessageKey/ID，查询到MQ的具体消息</td>
        <td><font color="red">No</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="green">Yes</font></td>
        <td><font color="red">No</font></td>
        <td>需要</td>
  	</tr>
  	<tr>
        <td><b>消费模式</b></td>
        <td></td>
        <td>stream模式</td>
        <td>流模式+队列模式</td>
        <td>广播模式+集群模式</td>
        <td>队列模式</td>
        <td>队列模式</td>
        <td>需要，根据场景选择消费模式</td>
  	</tr>
  	<tr>
        <td><b>消息可靠性</b></td>
        <td>以生产的消息，发送到mq,防止丢失</td>
        <td>request.required.acks</td>
        <td>Ack Quorum Size(Qa)</td>
        <td>RocketMQ与Kafka类似</td>
        <td>RabbitMQ是主从架构，通过镜像环形队列实现多副本及强一致性语义的</td>
        <td>NSQ会通过go-diskqueue组件将消息落盘到本地文件中，通过mem-queue-size参数控制内存中队列大小，如果mem-queue-size=0每条消息都会存储到磁盘里，不用担心节点重启引起的消息丢失。但由于是存储在本地磁盘中，如果节点离线，堆积在节点磁盘里的消息会丢失</td>
        <td><font color="red">非常重要<font></td>
  	</tr>
    <tr >
  	    <td rowspan="3"><b>性能</b></td>
        <td><b>单机吞吐量</b></td>
        <td></td>
        <td>605MB/S</td>
        <td>605MB/S</td>
        <td>大概500MB/S</td>
        <td>38MB/S</td>
        <td>?</td>
        <td><font color="red">重要<font></td>
  	</tr>
    <tr >
        <td><b>消息延迟</b></td>
        <td></td>
        <td>5ms</td>
        <td>5ms</td>
        <td>ms级</td>
        <td>us级</td>
        <td>？</td>
        <td><font color="red">非常重要<font></td>
  	</tr>
    <tr >
        <td><b>支持Topics数</b></td>
        <td></td>
        <td>百~千，过多会影响性能</td>
        <td>百万个</td>
        <td>百~千</td>
        <td>几千</td>
        <td>?</td>
        <td></td>
  	</tr>
    <tr >
  	    <td rowspan="3"><b>运维与可靠性</b></td>
        <td><b>高可用</b></td>
        <td></td>
        <td>分布式架构</td>
        <td>分布式架构</td>
        <td>Master/Slave</td>
        <td>Master/Slave</td>
        <td>分布式架构</td>
        <td><font color="red">非常重要<font></td>
  	</tr>
    <tr >
        <td><b>集群扩容</b></td>
        <td></td>
        <td>增加node,node之间会复制数据均衡</td>
        <td>增加node,通过新增加分片进行负载均衡</td>
        <td>增加节点</td>
        <td>增加节点</td>
        <td>增加节点</td>
        <td></td>
  	</tr>
    <tr >
        <td><b>异地容灾</b></td>
        <td></td>
        <td>可</td>
        <td>可</td>
        <td></td>
        <td></td>
        <td></td>
  	</tr>
  </table>

# 3: Kafka 特性

# 4: Pulsar 特性

# 5: Kafka 和 Pulsar 对比
