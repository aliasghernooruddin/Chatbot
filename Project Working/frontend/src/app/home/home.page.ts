import { Component, NgZone, OnInit, ViewChild } from "@angular/core";
import { Router } from '@angular/router';
import * as _ from "lodash";
import { DatabaseService, UtilService, MessageType } from '../providers';

@Component({
  selector: 'page-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss']
})

export class HomePage implements OnInit {

  messages: any[];

  public messageType = MessageType;
  @ViewChild('ionTxtArea') ionTxtArea;
  public txtArea: any;
  public lineHeight: number;
  public placeholder: string;
  public maxHeight: number;
  public maxExpand: number;

  chat: string = ''

  constructor(public _zone: NgZone,
    public databaseService: DatabaseService, private router: Router) {
    this.lineHeight = 20;
    this.maxExpand = 5;
    this.maxHeight = this.lineHeight * this.maxExpand;

    this.messages = [
      { type: 'message_response', message: "I am Helexa!!", epoch: Date.now(), data_type: "string" },
      { type: 'message_response', message: "Welcome to Hamdard Chatbot", epoch: Date.now(), data_type: "string" },
      { type: 'message_response', message: this.databaseService.name + " you can ask me anything", epoch: Date.now(), data_type: "string" },
      { type: 'message_response', message: "I am here for your help", epoch: Date.now(), data_type: "string" }
    ];
  }


  formatEpoch(epoch): string {
    return UtilService.getCalendarDay(epoch);
  }


  public sendMessage() {
    let message = {
      type: 'message_request',
      message: this.chat,
      epoch: Date.now()
    }
    this.messages.push(message)
    let data = {
      query: this.chat
    }
    this.databaseService.predict(data).subscribe(res => {
      let message = {
        type: 'message_response',
        message: res,
        epoch: Date.now(),
        data_type: typeof (res)
      }
      console.log(typeof (res));
      this.messages.push(message)
      this.chat = ''
    })
  }


  ngAfterViewInit() {
    this.txtArea = this.ionTxtArea.el;
    this.txtArea.style.height = this.lineHeight + "px";
    this.maxHeight = this.lineHeight * this.maxExpand;
    this.txtArea.style.resize = 'none';
  }

  logout() {
    this.messages = [{ type: 'message_response', message: "I am Helexa!!", epoch: Date.now(), data_type: "string" },
    { type: 'message_response', message: "Welcome to Hamdard Chatbot", epoch: Date.now(), data_type: "string" },
    { type: 'message_response', message: this.databaseService.name  + " you can ask me anything", epoch: Date.now(), data_type: "string" },
    { type: 'message_response', message: "I am here for your help", epoch: Date.now(), data_type: "string" }]
    this.router.navigateByUrl('login');
    window.location.replace('http://localhost:8100/login')
  }

  ngOnInit() {
  }

}
