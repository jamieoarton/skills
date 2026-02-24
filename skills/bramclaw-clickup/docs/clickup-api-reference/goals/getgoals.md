# Get Goals

View the Goals available in a Workspace.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_id}/goal": {
      "get": {
        "summary": "Get Goals",
        "tags": [
          "Goals"
        ],
        "description": "View the Goals available in a Workspace.",
        "operationId": "GetGoals",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "include_completed",
            "in": "query",
            "description": "",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetGoalsresponse",
                  "required": [
                    "goals",
                    "folders"
                  ],
                  "type": "object",
                  "properties": {
                    "goals": {
                      "type": "array",
                      "items": {
                        "title": "Goal2",
                        "required": [
                          "id",
                          "pretty_id",
                          "name",
                          "team_id",
                          "creator",
                          "owner",
                          "color",
                          "date_created",
                          "start_date",
                          "due_date",
                          "description",
                          "private",
                          "archived",
                          "multiple_owners",
                          "editor_token",
                          "date_updated",
                          "last_update",
                          "folder_id",
                          "pinned",
                          "owners",
                          "key_result_count",
                          "members",
                          "group_members",
                          "percent_completed"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "pretty_id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "team_id": {
                            "type": "string"
                          },
                          "creator": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "owner": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "color": {
                            "type": "string"
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "start_date": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "due_date": {
                            "type": "string"
                          },
                          "description": {
                            "type": "string"
                          },
                          "private": {
                            "type": "boolean"
                          },
                          "archived": {
                            "type": "boolean"
                          },
                          "multiple_owners": {
                            "type": "boolean"
                          },
                          "editor_token": {
                            "type": "string"
                          },
                          "date_updated": {
                            "type": "string"
                          },
                          "last_update": {
                            "type": "string"
                          },
                          "folder_id": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "pinned": {
                            "type": "boolean"
                          },
                          "owners": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "key_result_count": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "members": {
                            "type": "array",
                            "items": {
                              "title": "Member1",
                              "required": [
                                "id",
                                "username",
                                "email",
                                "color",
                                "permission_level",
                                "profilePicture",
                                "initials",
                                "isCreator"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "username": {
                                  "type": "string"
                                },
                                "email": {
                                  "type": "string"
                                },
                                "color": {
                                  "type": "string"
                                },
                                "permission_level": {
                                  "type": "string"
                                },
                                "profilePicture": {
                                  "type": "string"
                                },
                                "initials": {
                                  "type": "string"
                                },
                                "isCreator": {
                                  "type": "boolean"
                                }
                              },
                              "examples": [
                                {
                                  "id": 182,
                                  "username": "Jane Doe",
                                  "email": "janedoe@gmail.com",
                                  "color": "#827718",
                                  "permission_level": "edit",
                                  "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                                  "initials": "JD",
                                  "isCreator": true
                                }
                              ]
                            },
                            "description": ""
                          },
                          "group_members": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "percent_completed": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          }
                        },
                        "examples": [
                          {
                            "id": "e53a033c-900e-462d-a849-4a216b06d930",
                            "pretty_id": "6",
                            "name": "Goal ABC",
                            "team_id": "512",
                            "creator": 182,
                            "owner": null,
                            "color": "#32a852",
                            "date_created": "1568044355026",
                            "start_date": null,
                            "due_date": "1568036964079",
                            "description": "Updated Goal Description",
                            "private": false,
                            "archived": false,
                            "multiple_owners": true,
                            "editor_token": "goal:792c3027-83a2-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485ed15e675",
                            "date_updated": "1626130440221",
                            "last_update": "1626132992152",
                            "folder_id": null,
                            "pinned": false,
                            "owners": [],
                            "key_result_count": 1,
                            "members": [
                              {
                                "id": 182,
                                "username": "Jane Doe",
                                "email": "janedoe@gmail.com",
                                "color": "#827718",
                                "permission_level": "edit",
                                "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                                "initials": "JD",
                                "isCreator": true
                              }
                            ],
                            "group_members": [],
                            "percent_completed": 0
                          }
                        ]
                      },
                      "description": ""
                    },
                    "folders": {
                      "type": "array",
                      "items": {
                        "title": "Folder2",
                        "required": [
                          "id",
                          "name",
                          "team_id",
                          "private",
                          "date_created",
                          "creator",
                          "goal_count",
                          "members",
                          "goals"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "team_id": {
                            "type": "string"
                          },
                          "private": {
                            "type": "boolean"
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "creator": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "goal_count": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "members": {
                            "type": "array",
                            "items": {
                              "title": "Member2",
                              "required": [
                                "id",
                                "email",
                                "username",
                                "color",
                                "permission_level",
                                "date_added",
                                "added_by",
                                "initials",
                                "profilePicture"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "email": {
                                  "type": "string"
                                },
                                "username": {
                                  "type": "string"
                                },
                                "color": {
                                  "type": "string"
                                },
                                "permission_level": {
                                  "type": "string"
                                },
                                "date_added": {
                                  "type": "integer",
                                  "contentEncoding": "int64"
                                },
                                "added_by": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "initials": {
                                  "type": "string"
                                },
                                "profilePicture": {
                                  "type": "string"
                                }
                              },
                              "examples": [
                                {
                                  "id": 182,
                                  "email": "janedoe@gmail.com",
                                  "username": "Jane Doe",
                                  "color": "#827718",
                                  "permission_level": "read",
                                  "date_added": 1631599941928,
                                  "added_by": 183,
                                  "initials": "JD",
                                  "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg"
                                }
                              ]
                            },
                            "description": ""
                          },
                          "goals": {
                            "type": "array",
                            "items": {
                              "title": "Goal3",
                              "required": [
                                "id",
                                "pretty_id",
                                "name",
                                "team_id",
                                "creator",
                                "owner",
                                "color",
                                "date_created",
                                "start_date",
                                "due_date",
                                "description",
                                "private",
                                "archived",
                                "multiple_owners",
                                "editor_token",
                                "date_updated",
                                "last_update",
                                "folder_id",
                                "folder_access",
                                "pinned",
                                "owners",
                                "key_result_count",
                                "members",
                                "group_members",
                                "percent_completed"
                              ],
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "pretty_id": {
                                  "type": "string"
                                },
                                "name": {
                                  "type": "string"
                                },
                                "team_id": {
                                  "type": "string"
                                },
                                "creator": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "owner": {
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                },
                                "color": {
                                  "type": "string"
                                },
                                "date_created": {
                                  "type": "string"
                                },
                                "start_date": {
                                  "type": [
                                    "string",
                                    "null"
                                  ]
                                },
                                "due_date": {
                                  "type": "string"
                                },
                                "description": {
                                  "type": "string"
                                },
                                "private": {
                                  "type": "boolean"
                                },
                                "archived": {
                                  "type": "boolean"
                                },
                                "multiple_owners": {
                                  "type": "boolean"
                                },
                                "editor_token": {
                                  "type": "string"
                                },
                                "date_updated": {
                                  "type": "string"
                                },
                                "last_update": {
                                  "type": "string"
                                },
                                "folder_id": {
                                  "type": "string"
                                },
                                "folder_access": {
                                  "type": "boolean"
                                },
                                "pinned": {
                                  "type": "boolean"
                                },
                                "owners": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "description": ""
                                },
                                "key_result_count": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                },
                                "members": {
                                  "type": "array",
                                  "items": {
                                    "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1goal/get/responses/200/content/application~1json/schema/properties/goals/items/properties/members/items"
                                  },
                                  "description": ""
                                },
                                "group_members": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  },
                                  "description": ""
                                },
                                "percent_completed": {
                                  "type": "integer",
                                  "contentEncoding": "int32"
                                }
                              },
                              "examples": [
                                {
                                  "id": "e53a033c-900e-462d-a849-4a216b06d930",
                                  "pretty_id": "8",
                                  "name": "Q1 Goals",
                                  "team_id": "512",
                                  "creator": 182,
                                  "owner": null,
                                  "color": "#32a852",
                                  "date_created": "1568044355026",
                                  "start_date": null,
                                  "due_date": "1568036964079",
                                  "description": "Goal for Q1",
                                  "private": false,
                                  "archived": false,
                                  "multiple_owners": true,
                                  "editor_token": "goal:792c3027-83b5-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485fc22d477",
                                  "date_updated": "1626130440221",
                                  "last_update": "1626132992152",
                                  "folder_id": "05921253-7737-44af-a1aa-36fd11244e6f",
                                  "folder_access": true,
                                  "pinned": false,
                                  "owners": [],
                                  "key_result_count": 1,
                                  "members": [
                                    {
                                      "id": 182,
                                      "username": "Jane Doe",
                                      "email": "janedoe@gmail.com",
                                      "color": "#827718",
                                      "permission_level": "edit",
                                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                                      "initials": "JD",
                                      "isCreator": true
                                    }
                                  ],
                                  "group_members": [],
                                  "percent_completed": 1
                                }
                              ]
                            },
                            "description": ""
                          }
                        },
                        "examples": [
                          {
                            "id": "05921253-7737-44af-a1aa-36fd11244e6f",
                            "name": "Quarterly Goals",
                            "team_id": "512",
                            "private": true,
                            "date_created": "1548802674671",
                            "creator": 182,
                            "goal_count": 1,
                            "members": [
                              {
                                "id": 182,
                                "email": "janedoe@gmail.com",
                                "username": "Jane Doe",
                                "color": "#827718",
                                "permission_level": "read",
                                "date_added": 1631599941928,
                                "added_by": 183,
                                "initials": "JD",
                                "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg"
                              }
                            ],
                            "goals": [
                              {
                                "id": "e53a033c-900e-462d-a849-4a216b06d930",
                                "pretty_id": "8",
                                "name": "Q1 Goals",
                                "team_id": "512",
                                "creator": 182,
                                "owner": null,
                                "color": "#32a852",
                                "date_created": "1568044355026",
                                "start_date": null,
                                "due_date": "1568036964079",
                                "description": "Goal for Q1",
                                "private": false,
                                "archived": false,
                                "multiple_owners": true,
                                "editor_token": "goal:792c3027-83b5-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485fc22d477",
                                "date_updated": "1626130440221",
                                "last_update": "1626132992152",
                                "folder_id": "05921253-7737-44af-a1aa-36fd11244e6f",
                                "folder_access": true,
                                "pinned": false,
                                "owners": [],
                                "key_result_count": 1,
                                "members": [
                                  {
                                    "id": 182,
                                    "username": "Jane Doe",
                                    "email": "janedoe@gmail.com",
                                    "color": "#827718",
                                    "permission_level": "edit",
                                    "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                                    "initials": "JD",
                                    "isCreator": true
                                  }
                                ],
                                "group_members": [],
                                "percent_completed": 1
                              }
                            ]
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "goals": [
                        {
                          "id": "e53a033c-900e-462d-a849-4a216b06d930",
                          "pretty_id": "6",
                          "name": "Goal ABC",
                          "team_id": "512",
                          "creator": 182,
                          "owner": null,
                          "color": "#32a852",
                          "date_created": "1568044355026",
                          "start_date": null,
                          "due_date": "1568036964079",
                          "description": "Updated Goal Description",
                          "private": false,
                          "archived": false,
                          "multiple_owners": true,
                          "editor_token": "goal:792c3027-83a2-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485ed15e675",
                          "date_updated": "1626130440221",
                          "last_update": "1626132992152",
                          "folder_id": null,
                          "pinned": false,
                          "owners": [],
                          "key_result_count": 1,
                          "members": [
                            {
                              "id": 182,
                              "username": "Jane Doe",
                              "email": "janedoe@gmail.com",
                              "color": "#827718",
                              "permission_level": "edit",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                              "initials": "JD",
                              "isCreator": true
                            }
                          ],
                          "group_members": [],
                          "percent_completed": 0
                        }
                      ],
                      "folders": [
                        {
                          "id": "05921253-7737-44af-a1aa-36fd11244e6f",
                          "name": "Quarterly Goals",
                          "team_id": "512",
                          "private": true,
                          "date_created": "1548802674671",
                          "creator": 182,
                          "goal_count": 1,
                          "members": [
                            {
                              "id": 182,
                              "email": "janedoe@gmail.com",
                              "username": "Jane Doe",
                              "color": "#827718",
                              "permission_level": "read",
                              "date_added": 1631599941928,
                              "added_by": 183,
                              "initials": "JD",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg"
                            }
                          ],
                          "goals": [
                            {
                              "id": "e53a033c-900e-462d-a849-4a216b06d930",
                              "pretty_id": "8",
                              "name": "Q1 Goals",
                              "team_id": "512",
                              "creator": 182,
                              "owner": null,
                              "color": "#32a852",
                              "date_created": "1568044355026",
                              "start_date": null,
                              "due_date": "1568036964079",
                              "description": "Goal for Q1",
                              "private": false,
                              "archived": false,
                              "multiple_owners": true,
                              "editor_token": "goal:792c3027-83b5-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485fc22d477",
                              "date_updated": "1626130440221",
                              "last_update": "1626132992152",
                              "folder_id": "05921253-7737-44af-a1aa-36fd11244e6f",
                              "folder_access": true,
                              "pinned": false,
                              "owners": [],
                              "key_result_count": 1,
                              "members": [
                                {
                                  "id": 182,
                                  "username": "Jane Doe",
                                  "email": "janedoe@gmail.com",
                                  "color": "#827718",
                                  "permission_level": "edit",
                                  "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                                  "initials": "JD",
                                  "isCreator": true
                                }
                              ],
                              "group_members": [],
                              "percent_completed": 1
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "goals": [
                    {
                      "id": "e53a033c-900e-462d-a849-4a216b06d930",
                      "pretty_id": "6",
                      "name": "Goal ABC",
                      "team_id": "512",
                      "creator": 182,
                      "owner": null,
                      "color": "#32a852",
                      "date_created": "1568044355026",
                      "start_date": null,
                      "due_date": "1568036964079",
                      "description": "Updated Goal Description",
                      "private": false,
                      "archived": false,
                      "multiple_owners": true,
                      "editor_token": "goal:792c3027-83a2-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485ed15e675",
                      "date_updated": "1626130440221",
                      "last_update": "1626132992152",
                      "folder_id": null,
                      "pinned": false,
                      "owners": [],
                      "key_result_count": 1,
                      "members": [
                        {
                          "id": 182,
                          "username": "Jane Doe",
                          "email": "janedoe@gmail.com",
                          "color": "#827718",
                          "permission_level": "edit",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                          "initials": "JD",
                          "isCreator": true
                        }
                      ],
                      "group_members": [],
                      "percent_completed": 0
                    }
                  ],
                  "folders": [
                    {
                      "id": "05921253-7737-44af-a1aa-36fd11244e6f",
                      "name": "Quarterly Goals",
                      "team_id": "512",
                      "private": true,
                      "date_created": "1548802674671",
                      "creator": 182,
                      "goal_count": 1,
                      "members": [
                        {
                          "id": 182,
                          "email": "janedoe@gmail.com",
                          "username": "Jane Doe",
                          "color": "#827718",
                          "permission_level": "read",
                          "date_added": 1631599941928,
                          "added_by": 183,
                          "initials": "JD",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg"
                        }
                      ],
                      "goals": [
                        {
                          "id": "e53a033c-900e-462d-a849-4a216b06d930",
                          "pretty_id": "8",
                          "name": "Q1 Goals",
                          "team_id": "512",
                          "creator": 182,
                          "owner": null,
                          "color": "#32a852",
                          "date_created": "1568044355026",
                          "start_date": null,
                          "due_date": "1568036964079",
                          "description": "Goal for Q1",
                          "private": false,
                          "archived": false,
                          "multiple_owners": true,
                          "editor_token": "goal:792c3027-83b5-45de-be96-2f623b5f9078:1626303240249:38fd99e8-f989-4125-9a05-19ead0ed83a6:57bdc749-4ca6-4082-a78e-3485fc22d477",
                          "date_updated": "1626130440221",
                          "last_update": "1626132992152",
                          "folder_id": "05921253-7737-44af-a1aa-36fd11244e6f",
                          "folder_access": true,
                          "pinned": false,
                          "owners": [],
                          "key_result_count": 1,
                          "members": [
                            {
                              "id": 182,
                              "username": "Jane Doe",
                              "email": "janedoe@gmail.com",
                              "color": "#827718",
                              "permission_level": "edit",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/profile.jpg",
                              "initials": "JD",
                              "isCreator": true
                            }
                          ],
                          "group_members": [],
                          "percent_completed": 1
                        }
                      ]
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Goals"
    }
  ]
}
```