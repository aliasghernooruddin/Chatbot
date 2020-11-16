import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { DatabaseService } from '../providers';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss'],
})
export class LoginPage implements OnInit {

    src: ""
    id = ""

    constructor(private router: Router, private db: DatabaseService) { }

    login() {
        if (this.id == '1182-2015') {
            this.db.id = '4lZ2opCNWKuZidJcWDPE'
            this.db.name = 'Saad Nasir'
        }
        if (this.id == '1263-2015') {
            this.db.id = '6aPCZWJhQGtrw33B3DUh'
            this.db.name = 'Balaj Yousuf'
        }
        if (this.id == '1226-2015') {
            this.db.id = 'xmnCjlOT79EdCYZzHPyT'
            this.db.name = 'Osama Amjad'
        }
        this.router.navigateByUrl('home');
    }

    ngOnInit() {
    }

}